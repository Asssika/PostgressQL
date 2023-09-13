from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRESQL_USER: str
    POSTGRESQL_PASS: str
    POSTGRESQL_DB: str

    class Config:
        env_file = '.env'
        enf_file_encoding = 'utf-8'


def get_settings() -> Settings:
    setting = Settings()
    print(setting.POSTGRESQL_USER)
    return setting
