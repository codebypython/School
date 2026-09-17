"""
VietLawAssist — FastAPI Application Entry Point
=================================================
Agent-04 (System Architect) — Backend Foundation.

Khởi tạo FastAPI app với:
    - CORS middleware (cho phép Frontend kết nối)
    - Lifespan events (init DB + load BM25 index khi startup)
    - Router registration (health, retrieve)
    - Auto-generated Swagger UI tại /docs
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.config import get_settings
from app.core.database import init_database
from app.api.routes.health import router as health_router
from app.api.routes.retrieve import router as retrieve_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan events.

    Startup:
        1. Khởi tạo database (tạo bảng nếu chưa có)
        2. Load BM25 index từ file pickle (nếu tồn tại)

    Shutdown:
        1. Log thông báo tắt server
    """
    settings = get_settings()

    # === STARTUP ===
    logger.info(f"🚀 Khởi động {settings.app_name} v{settings.app_version}")
    logger.info(f"   Môi trường: {settings.app_env}")
    logger.info(f"   Database: {settings.database_path}")

    # 1. Khởi tạo database
    try:
        init_database()
        logger.success("✅ Database đã sẵn sàng")
    except Exception as e:
        logger.error(f"❌ Lỗi khởi tạo database: {e}")

    # 2. Load BM25 index (nếu có)
    try:
        from app.services.bm25_service import bm25_service
        bm25_service.load_index()
        if bm25_service.is_loaded:
            logger.success(
                f"✅ BM25 index đã load: {bm25_service.corpus_size} documents"
            )
        else:
            logger.warning(
                "⚠️ BM25 index chưa tồn tại. "
                "Chạy 'python scripts/ingest_db.py' để build index."
            )
    except Exception as e:
        logger.warning(f"⚠️ Không thể load BM25 index: {e}")

    yield

    # === SHUTDOWN ===
    logger.info(f"🛑 Tắt {settings.app_name}")


def create_app() -> FastAPI:
    """
    Factory function tạo FastAPI app.
    Tuân thủ Factory Pattern cho dễ testing.
    """
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=(
            "Hệ thống Hỗ trợ Tra cứu Pháp luật Đại cương — "
            "So sánh 4 phương pháp ML: BM25, PhoBERT+FAISS, RAG, Fine-tuned RAG. "
            "PBL6 Đồ án Chuyên ngành — ĐH Bách Khoa Đà Nẵng (DUT) K2023."
        ),
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # --- CORS Middleware ---
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # --- Register Routers ---
    app.include_router(health_router)
    app.include_router(retrieve_router)

    return app


# Tạo app instance (Uvicorn sẽ import object này)
app = create_app()
