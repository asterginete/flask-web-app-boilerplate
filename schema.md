## Database Schema Visualization

### User Table

| Field           | Type        | Properties              |
|-----------------|-------------|-------------------------|
| id              | Integer     | PK, Auto-increment      |
| username        | String      | Unique, Not Null        |
| email           | String      | Unique, Not Null        |
| hashed_password | String      | Not Null                |
| date_registered | DateTime    | Default: Current Time   |
| last_login      | DateTime    |                         |
| profile_id      | ForeignKey  | Profile.id              |

### Profile Table

| Field           | Type        | Properties              |
|-----------------|-------------|-------------------------|
| id              | Integer     | PK, Auto-increment      |
| user_id         | ForeignKey  | User.id, Unique         |
| first_name      | String      |                         |
| last_name       | String      |                         |
| bio             | Text        |                         |
| profile_picture | String      |                         |
| date_of_birth   | Date        |                         |

### SearchHistory Table (Optional)

| Field          | Type        | Properties              |
|----------------|-------------|-------------------------|
| id             | Integer     | PK, Auto-increment      |
| user_id        | ForeignKey  | User.id                 |
| query          | String      | Not Null                |
| date_searched  | DateTime    | Default: Current Time   |

### EmailNotifications Table (Optional)

| Field       | Type        | Properties              |
|-------------|-------------|-------------------------|
| id          | Integer     | PK, Auto-increment      |
| user_id     | ForeignKey  | User.id                 |
| email_type  | String      |                         |
| date_sent   | DateTime    | Default: Current Time   |
```
