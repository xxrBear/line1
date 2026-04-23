PYTHON := python3
MANAGE := $(PYTHON) manage.py

.PHONY: run migrate makemigrations shell superuser test help

help:
	@echo "Available commands:"
	@echo "  make run            # 启动开发服务器"
	@echo "  make makemigrations # 生成迁移文件"
	@echo "  make migrate        # 执行迁移"
	@echo "  make shell          # Django shell"
	@echo "  make superuser      # 创建管理员"
	@echo "  make test           # 运行测试"

run:
	$(MANAGE) runserver

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

shell:
	$(MANAGE) shell

superuser:
	$(MANAGE) createsuperuser

test:
	$(MANAGE) test

