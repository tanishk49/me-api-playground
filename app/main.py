from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, database, schemas

# ------------------ APP SETUP ------------------
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE
    allow_headers=["*"],  # Authorization, Content-Type
)

# Create DB tables
models.Base.metadata.create_all(bind=database.engine)


# ------------------ HEALTH ------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}


# ------------------ CREATE ------------------
@app.post("/profiles", response_model=schemas.ProfileResponse)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(database.get_db)):
    # base profile
    db_profile = models.Profile(
        name=profile.name,
        email=profile.email,
        education=profile.education,
        github=profile.github,
        linkedin=profile.linkedin,
        portfolio=profile.portfolio,
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)

    # skills
    for skill in profile.skills:
        db.add(models.Skill(name=skill.name, profile_id=db_profile.id))

    # projects
    for project in profile.projects:
        db.add(models.Project(
            title=project.title,
            description=project.description,
            link=project.link,
            profile_id=db_profile.id
        ))

    # work
    for work in profile.work:
        db.add(models.Work(
            company=work.company,
            role=work.role,
            duration=work.duration,
            profile_id=db_profile.id
        ))

    db.commit()
    db.refresh(db_profile)
    return db_profile


# ------------------ READ (ALL) ------------------
@app.get("/profiles", response_model=list[schemas.ProfileResponse])
def get_profiles(db: Session = Depends(database.get_db)):
    return db.query(models.Profile).all()


# ------------------ READ (ONE) ------------------
@app.get("/profiles/{profile_id}", response_model=schemas.ProfileResponse)
def get_profile(profile_id: int, db: Session = Depends(database.get_db)):
    profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


# ------------------ UPDATE ------------------
@app.put("/profiles/{profile_id}", response_model=schemas.ProfileResponse)
def update_profile(profile_id: int, profile_data: schemas.ProfileCreate, db: Session = Depends(database.get_db)):
    profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    # update base info
    profile.name = profile_data.name
    profile.email = profile_data.email
    profile.education = profile_data.education
    profile.github = profile_data.github
    profile.linkedin = profile_data.linkedin
    profile.portfolio = profile_data.portfolio

    # reset skills
    profile.skills.clear()
    for skill in profile_data.skills:
        db.add(models.Skill(name=skill.name, profile_id=profile.id))

    # reset projects
    profile.projects.clear()
    for project in profile_data.projects:
        db.add(models.Project(
            title=project.title,
            description=project.description,
            link=project.link,
            profile_id=profile.id
        ))

    # reset work
    profile.work.clear()
    for work in profile_data.work:
        db.add(models.Work(
            company=work.company,
            role=work.role,
            duration=work.duration,
            profile_id=profile.id
        ))

    db.commit()
    db.refresh(profile)
    return profile


# ------------------ DELETE ------------------
@app.delete("/profiles/{profile_id}")
def delete_profile(profile_id: int, db: Session = Depends(database.get_db)):
    profile = db.query(models.Profile).filter(models.Profile.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    db.delete(profile)
    db.commit()
    return {"detail": f"Profile with id {profile_id} has been deleted"}


# ------------------ PROJECT QUERY ------------------
@app.get("/projects", response_model=list[schemas.ProjectResponse])
def get_projects(skill: str | None = Query(None), db: Session = Depends(database.get_db)):
    query = db.query(models.Project)
    if skill:
        query = query.join(models.Profile).join(models.Skill).filter(func.lower(models.Skill.name) == skill.lower())
    return query.all()


# ------------------ TOP SKILLS ------------------
@app.get("/skills/top", response_model=list[schemas.SkillResponse])
def get_top_skills(limit: int = 10, db: Session = Depends(database.get_db)):
    results = (
        db.query(models.Skill.name, func.count(models.Skill.id).label("count"))
        .group_by(models.Skill.name)
        .order_by(func.count(models.Skill.id).desc())
        .limit(limit)
        .all()
    )
    # Map DB tuples → SkillResponse objects
    return [schemas.SkillResponse(id=i + 1, name=row[0]) for i, row in enumerate(results)]


# ------------------ SEARCH ------------------
@app.get("/search", response_model=list[schemas.ProfileResponse])
def search(q: str = Query(...), db: Session = Depends(database.get_db)):
    qstr = f"%{q.lower()}%"
    profiles = (
        db.query(models.Profile)
        .join(models.Project, isouter=True)
        .filter(
            func.lower(models.Profile.name).like(qstr) |
            func.lower(models.Project.title).like(qstr) |
            func.lower(models.Project.description).like(qstr)
        )
        .all()
    )
    return profiles
