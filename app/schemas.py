from pydantic import BaseModel
from typing import List, Optional


# ---------- Base Schemas ----------
class SkillBase(BaseModel):
    name: str


class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    link: Optional[str] = None


class WorkBase(BaseModel):
    company: str
    role: Optional[str] = None
    duration: Optional[str] = None


# ---------- Create Schema ----------
class ProfileCreate(BaseModel):
    name: str
    email: str
    education: Optional[str] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    portfolio: Optional[str] = None
    skills: List[SkillBase] = []
    projects: List[ProjectBase] = []
    work: List[WorkBase] = []


# ---------- Response Schemas ----------
class SkillResponse(SkillBase):
    id: int

    class Config:
        from_attributes = True   # Pydantic v2 replacement for orm_mode


class ProjectResponse(ProjectBase):
    id: int

    class Config:
        from_attributes = True


class WorkResponse(WorkBase):
    id: int

    class Config:
        from_attributes = True


class ProfileResponse(ProfileCreate):
    id: int
    skills: List[SkillResponse] = []
    projects: List[ProjectResponse] = []
    work: List[WorkResponse] = []

    class Config:
        from_attributes = True
