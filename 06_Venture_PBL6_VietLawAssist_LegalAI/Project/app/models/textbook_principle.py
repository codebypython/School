"""
VietLawAssist — Textbook Principle Pydantic Models
===================================================
Định nghĩa schema cho lý luận và nguyên lý từ Giáo trình PLĐC (Bộ GD&ĐT).
Tuân thủ Clean Architecture: tầng Domain/Entity.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class TextbookPrincipleBase(BaseModel):
    """Schema cơ bản cho một nguyên lý lý luận giáo trình."""
    id: str = Field(
        ...,
        description="Mã định danh duy nhất. VD: GT_PLDC_QPPL_STRUCTURE",
        examples=["GT_PLDC_QPPL_STRUCTURE", "GT_PLDC_VPPL_ELEMENTS"]
    )
    topic_code: str = Field(
        ...,
        description="Mã chủ đề tương ứng dạng đề thi",
        examples=["QPPL_STRUCTURE", "VPPL_ELEMENTS", "TRUE_FALSE", "CIVIL_INHERIT", "CRIMINAL_AGE"]
    )
    chapter: str = Field(
        ...,
        description="Tên chương trong giáo trình",
        examples=["Chương 2: Quy phạm pháp luật và Quan hệ pháp luật"]
    )
    framework_title: str = Field(
        ...,
        description="Tên khung lý luận hoặc barem",
        examples=["Cơ cấu ba bộ phận của Quy phạm pháp luật"]
    )
    rules_json: str = Field(
        ...,
        description="Cấu trúc barem chuẩn JSON (các mục bắt buộc phải có)"
    )
    theory_content: str = Field(
        ...,
        description="Nội dung lý luận trích dẫn từ giáo trình chuẩn"
    )


class TextbookPrincipleCreate(TextbookPrincipleBase):
    """Schema cho việc nạp nguyên lý vào database."""
    pass


class TextbookPrincipleInDB(TextbookPrincipleBase):
    """Schema cho nguyên lý đã lưu trong DB."""
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
