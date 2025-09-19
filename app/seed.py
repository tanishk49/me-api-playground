from sqlalchemy.orm import Session
from . import models, database

def seed():
    db: Session = database.SessionLocal()

    # delete existing for idempotency (careful in prod)
    db.query(models.Skill).delete()
    db.query(models.Project).delete()
    db.query(models.Work).delete()
    db.query(models.Profile).delete()
    db.commit()

    p = models.Profile(
        name="Your Name",
        email="you@example.com",
        education="B.Tech in CS",
        github="github.com/your",
        linkedin="linkedin.com/in/your",
        portfolio="your.site"
    )
    db.add(p)
    db.commit()
    db.refresh(p)

    # skills
    for s in ["Python","FastAPI","SQL","Docker"]:
        db.add(models.Skill(name=s, profile_id=p.id))

    # project
    db.add(models.Project(title="Portfolio API", description="Small FastAPI backend", link="https://github.com/you/repo", profile_id=p.id))

    # work
    db.add(models.Work(company="ABC Corp", role="Intern", duration="6 months", profile_id=p.id))
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()
