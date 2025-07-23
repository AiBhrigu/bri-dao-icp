#!/bin/bash

echo "🔧 Installing dependencies..."
sudo apt-get update
sudo apt-get install -y pandoc texlive-xetex fonts-dejavu

echo "📁 Ensuring directory structure exists..."
mkdir -p .github/workflows
mkdir -p docs

echo "📝 Creating GitHub Actions workflow..."
cat > .github/workflows/build-pdf.yml << 'EOF'
name: Build Whitepaper PDFs

on:
  push:
    branches: [ main ]
    paths:
      - 'docs/Whitepaper_*.md'

jobs:
  build-pdfs:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repo
      uses: actions/checkout@v4

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y pandoc texlive-xetex fonts-dejavu

    - name: Build PDF from EN Markdown
      run: |
        pandoc docs/Whitepaper_EN.md -o docs/Whitepaper_EN.pdf --pdf-engine=xelatex -V mainfont="DejaVu Serif"

    - name: Build PDF from RU Markdown
      run: |
        pandoc docs/Whitepaper_RU.md -o docs/Whitepaper_RU.pdf --pdf-engine=xelatex -V mainfont="DejaVu Serif"

    - name: Commit and push PDFs to main branch
      uses: stefanzweifel/git-auto-commit-action@v5
      with:
        commit_message: "Auto-generate Whitepaper PDFs"
        file_pattern: docs/*.pdf
        commit_user_name: github-actions[bot]
        commit_user_email: github-actions[bot]@users.noreply.github.com
        commit_author: AiBhrigu <154300034+AiBhrigu@users.noreply.github.com>
EOF

echo "✅ All setup! Now you can push changes to Whitepaper_*.md to auto-generate PDFs."
