# 📚 NoteNukkad — Hyperlocal Books & Notes Classifieds Backend

A scalable Django REST Framework backend enabling students to buy & sell second-hand books, handwritten notes, and study materials within their local area (city/pincode).

## 🚀 Key Features

- 🔐 JWT authentication — secure login/signup
- 📍 Location-based listing discovery (city + pincode filters)
- 🧭 Full CRUD for listings
- ⭐ Favorites system (save liked items)
- ⏱ Rate-limiting to prevent abuse
- ⚡ Redis cache ready for production performance
- 📑 Auto-generated API docs — Swagger & Redoc
- 🛠 Admin dashboard for moderation

---

## 🧱 Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Django + DRF |
| Database | PostgreSQL (SQLite in local dev) |
| Cache | Redis (production only) |
| Auth | JWT (SimpleJWT) |
| Docs | drf-yasg |

---

## 🔗 API Documentation

| Type | URL (Local Dev) |
|------|----------------|
| Swagger UI | `http://127.0.0.1:8000/swagger/` |
| Redoc | `http://127.0.0.1:8000/redoc/` |

---

## 🗂 Database Schema Summary

### User Model
