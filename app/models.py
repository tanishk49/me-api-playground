from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    education = Column(String, nullable=True)
    github = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
    portfolio = Column(String, nullable=True)

    # Relationships with cascade delete-orphan
    skills = relationship(
        "Skill", back_populates="profile", cascade="all, delete-orphan"
    )
    projects = relationship(
        "Project", back_populates="profile", cascade="all, delete-orphan"
    )
    work = relationship(
        "Work", back_populates="profile", cascade="all, delete-orphan"
    )


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)

    profile = relationship("Profile", back_populates="skills")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    link = Column(String, nullable=True)
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)

    profile = relationship("Profile", back_populates="projects")


class Work(Base):
    __tablename__ = "work"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)

    profile = relationship("Profile", back_populates="work")
