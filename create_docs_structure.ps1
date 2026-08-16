# ============================================================
# SMIP V2 - Databricks Documentation Structure
# Creates the complete docs folder hierarchy
# Author: Sumanth Vempalle
# ============================================================

$root = "docs"

# ------------------------------------------------------------
# Folder Structure
# ------------------------------------------------------------

$folders = @(
    "$root",

    "$root/01_overview",
    "$root/02_architecture",
    "$root/03_data_model",
    "$root/04_data_engineering",
    "$root/05_business_intelligence",
    "$root/06_user_guide",
    "$root/07_development",

    "$root/08_images",
    "$root/08_images/architecture",
    "$root/08_images/dashboards",
    "$root/08_images/lineage",
    "$root/08_images/schemas",
    "$root/08_images/logos"
)

foreach ($folder in $folders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "Created folder: $folder"
    }
}

# ------------------------------------------------------------
# Markdown Files
# ------------------------------------------------------------

$files = @(

    "$root/README.md",

    "$root/01_overview/README.md",
    "$root/01_overview/project_overview.md",
    "$root/01_overview/business_problem.md",
    "$root/01_overview/objectives.md",
    "$root/01_overview/project_scope.md",

    "$root/02_architecture/README.md",
    "$root/02_architecture/system_architecture.md",
    "$root/02_architecture/lakehouse_architecture.md",
    "$root/02_architecture/medallion_architecture.md",
    "$root/02_architecture/pipeline_architecture.md",
    "$root/02_architecture/technology_stack.md",

    "$root/03_data_model/README.md",
    "$root/03_data_model/manufacturing_process.md",
    "$root/03_data_model/event_model.md",
    "$root/03_data_model/star_schema.md",
    "$root/03_data_model/dimensions.md",
    "$root/03_data_model/facts.md",
    "$root/03_data_model/business_keys.md",

    "$root/04_data_engineering/README.md",
    "$root/04_data_engineering/bronze_layer.md",
    "$root/04_data_engineering/silver_layer.md",
    "$root/04_data_engineering/dimensions.md",
    "$root/04_data_engineering/facts.md",
    "$root/04_data_engineering/gold_layer.md",
    "$root/04_data_engineering/expectations.md",
    "$root/04_data_engineering/pipeline_execution.md",

    "$root/05_business_intelligence/README.md",
    "$root/05_business_intelligence/manufacturing_kpis.md",
    "$root/05_business_intelligence/sql_dashboard.md",
    "$root/05_business_intelligence/dashboard_walkthrough.md",
    "$root/05_business_intelligence/executive_metrics.md",

    "$root/06_user_guide/README.md",
    "$root/06_user_guide/environment_setup.md",
    "$root/06_user_guide/deployment.md",
    "$root/06_user_guide/running_the_pipeline.md",
    "$root/06_user_guide/dashboard_usage.md",
    "$root/06_user_guide/troubleshooting.md",

    "$root/07_development/README.md",
    "$root/07_development/project_journey.md",
    "$root/07_development/architecture_decisions.md",
    "$root/07_development/branch_strategy.md",
    "$root/07_development/roadmap.md",
    "$root/07_development/lessons_learned.md"
)

foreach ($file in $files) {
    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
        Write-Host "Created file: $file"
    }
}

Write-Host ""
Write-Host "==============================================="
Write-Host "SMIP Databricks documentation structure created!"
Write-Host "==============================================="