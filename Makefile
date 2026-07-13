PYTHON  := python3
UV      := $(shell command -v uv 2>/dev/null || echo $(HOME)/.local/bin/uv)
MANAGE  := $(UV) run $(PYTHON) manage.py

.DEFAULT_GOAL := help
.PHONY: help run migrate makemigrations shell superuser test check dist setup install-uv

help:
	@echo "Available commands:"
	@echo "  make setup          # 安装 uv 并同步依赖"
	@echo "  make run            # 启动开发服务器"
	@echo "  make makemigrations # 生成迁移文件"
	@echo "  make migrate        # 执行迁移"
	@echo "  make shell          # Django shell"
	@echo "  make check          # 运行检查"
	@echo "  make superuser      # 创建管理员"
	@echo "  make test           # 运行测试"
	@echo "  make dist           # 收集静态文件"

install-uv:
ifeq ($(wildcard $(UV)),)
	@echo "uv not found, installing..."
	curl -LsSf https://astral.sh/uv/install.sh | sh
else
	@echo "uv already installed at $(UV)"
endif

setup: install-uv
	$(UV) sync

run:
	$(MANAGE) runserver

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

shell:
	$(MANAGE) shell

check:
	$(MANAGE) check

superuser:
	$(MANAGE) createsuperuser

test:
	$(MANAGE) test

dist:
	$(MANAGE) collectstatic --noinput
