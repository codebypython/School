"""
VietLawAssist — Application Configuration
==========================================
Sử dụng Pydantic Settings để load config từ biến môi trường (.env file).
Tuân thủ RULES-SAFETY-GOVERNANCE: Zero Secrets in Code.
"""

from pathlib import Path
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


# --- Đường dẫn gốc của dự án ---
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """
    Cấu hình ứng dụng — tất cả giá trị nhạy cảm phải nạp từ .env.
    Không bao giờ hardcode secrets vào source code.
    """

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --- Application ---
    app_name: str = "VietLawAssist"
    app_version: str = "1.0.0"
    app_env: str = "development"
    debug: bool = True

    # --- Server ---
    host: str = "0.0.0.0"
    port: int = 8000

    # --- Database ---
    database_url: str = f"sqlite:///{BASE_DIR / 'data' / 'law_corpus.db'}"

    @property
    def database_path(self) -> Path:
        """Trích xuất đường dẫn file SQLite từ URL."""
        db_path_str = self.database_url.replace("sqlite:///", "")
        return Path(db_path_str)

    # --- BM25 Configuration ---
    bm25_k1: float = 1.5
    bm25_b: float = 0.75
    bm25_top_k: int = 5
    bm25_index_path: str = str(BASE_DIR / "data" / "bm25_index.pkl")

    # --- Tokenizer ---
    tokenizer: str = "pyvi"  # "pyvi" | "underthesea"

    # --- Logging ---
    log_level: str = "INFO"
    log_file: str = str(BASE_DIR / "logs" / "app.log")

    # --- CORS ---
    cors_origins: str = "http://localhost:3000,http://localhost:5173"

    @property
    def cors_origin_list(self) -> list[str]:
        """Parse CORS origins string thành list."""
        return [origin.strip() for origin in self.cors_origins.split(",")]


@lru_cache()
def get_settings() -> Settings:
    """
    Singleton pattern: chỉ tạo Settings object một lần duy nhất.
    Sử dụng lru_cache để tránh đọc lại .env file mỗi request.
    """
    return Settings()
