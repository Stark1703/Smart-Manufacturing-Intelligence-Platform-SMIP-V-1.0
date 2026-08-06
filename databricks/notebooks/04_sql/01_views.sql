-- ============================================================================
-- Smart Manufacturing Intelligence Platform (SMIP)
-- SQL Views
--
-- Description:
-- Business views for Power BI and SQL analytics.
--
-- Author : Sumanth Vempalle
-- Version: 1.0.0
-- ============================================================================

CREATE OR REPLACE VIEW smip.gold.vw_production_summary AS
SELECT *
FROM smip.gold.production_summary;

CREATE OR REPLACE VIEW smip.gold.vw_quality_summary AS
SELECT *
FROM smip.gold.quality_summary;

CREATE OR REPLACE VIEW smip.gold.vw_oee_summary AS
SELECT *
FROM smip.gold.oee_summary;

CREATE OR REPLACE VIEW smip.gold.vw_traceability_summary AS
SELECT *
FROM smip.gold.traceability_summary;

CREATE OR REPLACE VIEW smip.gold.vw_executive_summary AS
SELECT *
FROM smip.gold.executive_summary;


