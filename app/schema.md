# Database Schema

This project uses **SQLite** with SQLAlchemy ORM.  
Schema is auto-created from `models.py`.  

---

## Tables & Columns

### 1. Profile
| Column     | Type     | Notes                  |
|------------|----------|------------------------|
| id         | Integer  | Primary Key            |
| name       | String   | Not Null               |
| email      | String   | Unique, Not Null       |
| education  | String   | Optional               |
| github     | String   | Optional (URL)         |
| linkedin   | String   | Optional (URL)         |
| portfolio  | String   | Optional (URL)         |

**Relationships**
- Profile → has many Skills
- Profile → has many Projects
- Profile → has many Work

---

### 2. Skill
| Column     | Type     | Notes                          |
|------------|----------|--------------------------------|
| id         | Integer  | Primary Key                    |
| name       | String   | Not Null                       |
| profile_id | Integer  | FK → Profile.id, Not Null      |

---

### 3. Project
| Column      | Type     | Notes                          |
|-------------|----------|--------------------------------|
| id          | Integer  | Primary Key                    |
| title       | String   | Not Null                       |
| description | Text     | Optional                       |
| link        | String   | Optional (URL)                 |
| profile_id  | Integer  | FK → Profile.id, Not Null      |

---

### 4. Work
| Column     | Type     | Notes                          |
|------------|----------|--------------------------------|
| id         | Integer  | Primary Key                    |
| company    | String   | Not Null                       |
| role       | String   | Optional                       |
| duration   | String   | Optional                       |
| profile_id | Integer  | FK → Profile.id, Not Null      |

---

## Relationships (ER-style)
