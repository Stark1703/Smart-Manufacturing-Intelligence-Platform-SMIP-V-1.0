# ============================================================
# Smart Manufacturing Intelligence Platform (SMIP)
# Repository Structure Setup
# Author: Sumanth Vempalle
# ============================================================

Write-Host ""
Write-Host "============================================="
Write-Host " Creating SMIP Project Structure"
Write-Host "============================================="
Write-Host ""

# ------------------------------------------------------------
# Root Folders
# ------------------------------------------------------------

$folders = @(

    "data\master_data",
    "data\transactional_data",

    "databricks",
    "databricks\notebooks",
    "databricks\notebooks\01_bronze",
    "databricks\notebooks\02_silver",
    "databricks\notebooks\03_gold",
    "databricks\notebooks\04_sql",
    "databricks\notebooks\05_ml",
    "databricks\workflows",
    "databricks\schemas",

    "docs",
    "docs\analytics",
    "docs\architecture",
    "docs\data_model",
    "docs\development",
    "docs\user_guide",
    "docs\images",
    "docs\images\architecture",
    "docs\images\workflow",
    "docs\images\er",
    "docs\images\dashboards",
    "docs\images\screenshots",

    "powerbi",
    "powerbi\reports",
    "powerbi\screenshots",
    "powerbi\themes",

    "sql",
    "sql\bronze",
    "sql\silver",
    "sql\gold",
    "sql\views",

    "tests"
)

foreach ($folder in $folders) {

    New-Item `
        -ItemType Directory `
        -Force `
        -Path $folder | Out-Null

}

Write-Host "Folders created."

# ------------------------------------------------------------
# .gitkeep Files
# ------------------------------------------------------------

$gitkeepFolders = @(

    "data\master_data",
    "data\transactional_data",

    "databricks\workflows",
    "databricks\schemas",

    "powerbi\reports",
    "powerbi\screenshots",
    "powerbi\themes",

    "sql\bronze",
    "sql\silver",
    "sql\gold",
    "sql\views",

    "tests"
)

foreach ($folder in $gitkeepFolders) {

    New-Item `
        -ItemType File `
        -Force `
        -Path "$folder\.gitkeep" | Out-Null

}

Write-Host ".gitkeep files created."

# ------------------------------------------------------------
# README Files
# ------------------------------------------------------------

$readmeFiles = @(
    "databricks\README.md",
    "powerbi\README.md",
    "sql\README.md",
    "tests\README.md",
    "data\README.md",
    "data\master_data\README.md",
    "data\transactional_data\README.md"
)

foreach ($file in $readmeFiles) {

    if (!(Test-Path $file)) {

        New-Item `
            -ItemType File `
            -Path $file | Out-Null

    }

}

Write-Host "README files created."

# ------------------------------------------------------------
# Completed
# ------------------------------------------------------------

Write-Host ""
Write-Host "============================================="
Write-Host " SMIP Repository Ready!"
Write-Host "============================================="
Write-Host ""