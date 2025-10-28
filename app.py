import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import time
from io import StringIO, BytesIO
from dotenv import load_dotenv
import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.colors import HexColor, black, whitesmoke, white, gray
from reportlab.lib.enums import TA_CENTER
from PIL import Image
import tempfile
import base64
import os
from datetime import datetime
from io import BytesIO

# Translation dictionaries for multilingual support
# English translations
EN = {
    # Sidebar elements
    "app_title": "SEDIVER Celsius AI",
    "control_panel": "Control Panel",
    "control_subtitle": "Specialized analysis for SEDIVER R&D team",
    "data_files": "📁 Data Files",
    "upload_files": "Upload thermal data files",
    "upload_help": "Upload position files (e.g., cz_position3.dat, 27517_recap_temperature.xlsx, etc.)",
    "select_analysis": "Select Analysis Type:",
    "select_position": "Select Position:",
    "upload_more": "📁 Please upload more positions above to see available options",
    "position_help": "Upload multiple position files (.dat, .xlsx, .csv) to enable position selection and analysis",
    "analysis_help": "Choose the type of analysis to perform",
    "language": "Language",
    
    # Analysis types
    "temp_curves": "Temperature Curves Over Time",
    "glass_shell": "Individual Glass Shell Analysis",
    "peak_temp": "Peak Temperature Summary",
    "multi_position": "Multi-Position Composite",
    "interactive": "Interactive Plotly View",
    "thermal_journey": "Full Line Thermal Journey",
    "ai_summary": "AI Summary & Reports",
    
    # Analysis section headers (expanders)
    "temp_curves_header": "🌡️ Temperature Curves Over Time",
    "glass_shell_header": "🔍 Individual Glass Shell Analysis",
    "peak_temp_header": "📊 Peak Temperature Summary",
    "multi_position_header": "🏭 Multi-Position Composite Analysis",
    "interactive_header": "🖼️ Interactive Plotly View",
    "thermal_journey_header": "📈 Full Line Thermal Journey",
    "ai_summary_header": "🧠 AI Summary & Reporting Assistant",
    "report_preview_header": "📄 Report Preview",
    
    # Subheaders
    "loaded_positions": "📁 Loaded Positions",
    "data_summary": "📊 Data Summary",
    "plateau_detection_settings": "Temperature Curves Over Time",
    "quality_insights": "📊 Quality Insights",
    "pdf_export": "📄 PDF Export",
    "shell_metrics": "📊 Shell Metrics",
    "peak_temp_data": "📋 Peak Temperature Data",
    "overall_statistics": "📈 Overall Statistics",
    "position_comparison": "📊 Position Comparison",
    "position_number": "Position {number}",
    "position_with_match": "Position {match}",
    "peak_temp_by_shell_title": "Peak Temperatures by Shell - {position}",
    "shell_number_axis": "Shell Number",
    "shell_duration_seconds": "Shell Duration (seconds)",
    "peak_temp_y_axis": "Peak Temperature (°C)",
    "glass_shell_journey_title": "Glass Shell Journey Across Time",
    "multi_position_journey_title": "Multi-Position Glass Shell Journey (Primary Sensor)",

    # Shell analysis metrics
    "duration": "Duration",
    "avg_peak_temp": "Avg Peak Temp",
    "temp_range": "Temp Range",
    "mean_peak_temp": "Mean Peak Temp",
    "temp_range_full": "Temp Range",
    "head_max": "Head Max",
    "avg_temperature": "Avg Temperature",
    "temperature_stability": "Temp Stability",
    "shell_quality": "Shell Quality",
    "total_shells": "Total Shells",
    "avg_cycle_time": "Avg Cycle Time",
    "production_rate": "Production Rate",
    "temp_max": "Max Temp (°C)",
    "temp_min": "Min Temp (°C)",
    "temp_avg": "Avg Temp (°C)",
    "duration": "Duration (s)",
    "samples": "Samples",
    "interactive_view": "Interactive Temperature View",
    "detailed_shell_analysis_title": "🔍 Detailed Analysis - Shell {shell_number}",
    "duration_metric": "Duration",
    "avg_temp_metric": "Avg Temp",
    "select_sensors": "Select Sensors:",
    "total_shells_detected": "Total Shells Detected",
    "avg_shell_duration": "Avg Shell Duration",
    "total_samples": "Total Samples",
    "sensors": "Sensors",
    
    "upload_multiple_files": "📁 Upload Multiple Position Files",
    "head_sensor_journey": "Primary Sensor Thermal Journey Comparison",
    "thermal_journey_insights": "📊 Thermal Journey Insights",
    "line_performance": "🎯 Line Performance Assessment",
    "ai_configuration": "🔑 AI Configuration",
    "report_type": "📊 Report Type",
    "ai_analysis_report": "📋 AI Analysis Report",
    "interactive_shell_analysis": "🔍 Interactive Shell Analysis",
    "download_options": "📥 Download Options",
    "upload_journey_files": "📁 Upload Multiple Files for Journey Report",
    "report_template_generator": "📋 Report Template Generator",
    "report_configuration": "⚙️ Report Configuration",
    "report_customization": "🎨 Report Customization",
    "report_sections": "📑 Report Sections",
    "data_selection": "📊 Data Selection",
    "live_preview": "👁️ Live Preview",
    "generate_download": "📥 Generate & Download",
    
    # Main content
    "upload_prompt": "⬅︎ Upload your toughening data files (.dat format) to begin thermal analysis",
    "expected_format": "📋 Expected Data Format",
    "file_naming": "📁 File Naming Convention:",
    "single_position": "Single position:",
    "multiple_positions": "Multiple positions:",
    "analysis_capabilities": "🎯 Analysis Capabilities:",
    "plateau_detection": "✅ Automatic plateau detection for glass shells",
    "peak_extraction": "✅ Peak temperature extraction",
    "production_rate": "✅ Production rate calculation (pcs/min)",
    "thermal_profiling": "✅ Multi-sensor thermal profiling",
    "journey_reconstruction": "✅ Cross-position journey reconstruction",
    "adjust_thresholds_tip": "🔧 Tip: Adjust thresholds to capture glass shells",
    
    # AI section
    "ai_enhancement": "🤖 AI Enhancement (Optional)",
    "enhance_with_ai": "🧠 Enhance with AI Analysis",
    "ai_help": "Use AI to generate intelligent insights and recommendations",
    "ai_key_required": "🔑 AI enhancement requires OpenAI API key (configure in AI Analysis tab)",
    "select_ai_sections": "Select AI-enhanced sections:",
    "ai_will_enhance": "✅ AI will enhance:",
    "upload_to_use": "📁 Please upload thermal data files to use the Report Template Generator",
    
    # Report sections
    "download_report": "📄 Download Report",
    "download_help": "Download your custom thermal analysis report",
    "generate_first": "Generate a report first to enable download",
    "executive_summary": "Executive Summary",
    "quality_assessment": "Quality Assessment",
    "recommendations": "Recommendations",
    "predictive_insights": "Predictive Insights",
    
    # Plateau Detection Interface
    "flatness_celsius": "Flatness (°C)",
    "plateau_min_seconds": "Plateau min (s)",
    "sensor_label": "Choose Side:",
    "no_plateau_found": "⚠️ No plateau found - try adjusting thresholds",
    "sensor_flatness_duration": "🔍 Sensor: {sensor} | Flatness: {flatness}°C | Min duration: {duration}s",
    "mobile_std_analysis": "📊 **Mobile Standard Deviation Analysis**: Avg σ = {avg_std:.2f}°C, Max σ = {max_std:.2f}°C, Stable regions = {stable_percentage:.1f}%",
    "flatness_threshold": "Flatness Threshold ({flatness}°C)",
    "temp_curves_with_std": "Temperature Curves with Mobile Standard Deviation Analysis - {position}",
    "mobile_std_celsius": "Mobile Standard Deviation (°C)",
    "time_seconds": "Time (seconds)",
    "temperature_celsius": "Temperature (°C)",

    # Shell Analysis
    "shell_analysis_title": "Shell Analysis #{shell_number} - {position}",
    "shell_duration": "Duration: {duration}s",
    "select_shell_number": "Select Shell Number:",
    "no_data_caption": "⚠️ No data: {sensor}",
    "head_peak": "Head Peak",
    "peak": "Peak",
    "shell_duration_slider": "Approximate Shell Duration (seconds)",
    "select_shell_help": "Choose which shell to analyze in detail",
    "positions_analyzed": "Positions Analyzed",
    "avg_max_temp": "Avg Max Temp",
    "temp_consistency": "Temp Consistency",
    "file": "File",
    "temp_range_celsius": "Temp Range (°C)",
    "position_changes_detected": "🔄 Position Changes Detected: {count}",
    "position_change_number": "Position Change #",
    "timestamp_seconds": "Timestamp (s)",
    "min_temperature_celsius": "Min Temperature (°C)",
    "between_shells": "Between Shells",
    "download_position_changes": "📥 Download Position Changes (CSV)",
    "position_changes_help": "Download the position changes analysis as CSV file"
}

# French translations
FR = {
    # Sidebar elements
    "app_title": "SEDIVER Celsius AI",
    "control_panel": "Tour de Contrôle",
    "control_subtitle": "Analyse spécialisée pour l'équipe R&D SEDIVER",
    "data_files": "📁 Fichiers de Données",
    "upload_files": "Télécharger des fichiers thermiques",
    "upload_help": "Télécharger des fichiers de position (ex: cz_position3.dat, 27517_recap_temperature.xlsx, etc.)",
    "select_analysis": "Sélectionner le Type d'Analyse:",
    "select_position": "Sélectionner la Position:",
    "upload_more": "📁 Rajoutez de positions",
    "position_help": "Téléchargez plusieurs fichiers de position (.dat, .xlsx, .csv) pour activer la sélection et l'analyse des positions",
    "analysis_help": "Choisissez le type d'analyse à effectuer",
    "language": "Langue",
    
    # Analysis types
    "temp_curves": "Courbes de Température dans le Temps",
    "glass_shell": "Analyse Individuelle de Coquille en Verre",
    "peak_temp": "Résumé des Températures Maximales",
    "multi_position": "Composite Multi-Positions",
    "interactive": "Vue Interactive Plotly",
    "thermal_journey": "Parcours Thermique Complet",
    "ai_summary": "Résumé IA & Rapports",
    
    # Analysis section headers (expanders)
    "temp_curves_header": "🌡️ Courbes de Température dans le Temps",
    "glass_shell_header": "🔍 Analyse Individuelle de Coquille en Verre",
    "peak_temp_header": "📊 Résumé des Températures Maximales",
    "multi_position_header": "🏭 Analyse Composite Multi-Positions",
    "interactive_header": "🖼️ Vue Interactive Plotly",
    "thermal_journey_header": "📈 Parcours Thermique Complet de la Ligne",
    "ai_summary_header": "🧠 Assistant de Résumé et Rapports IA",
    "report_preview_header": "📄 Aperçu du Rapport",
    
    # Subheaders
    "loaded_positions": "📁 Positions Chargées",
    "data_summary": "📊 Résumé des Données",
    "plateau_detection_settings": "Courbes de Température dans le Temps",
    "quality_insights": "📊 Aperçus Qualité",
    "pdf_export": "📄 Export PDF",
    "shell_metrics": "📊 Métriques des Coquilles",
    "peak_temp_data": "📋 Données de Température Maximale",
    "overall_statistics": "📈 Statistiques Générales",
    "position_comparison": "📊 Comparaison des Positions",
    "position_number": "Position {number}",
    "position_with_match": "Position {match}",
    "peak_temp_by_shell_title": "Températures Maximales par Coquille - {position}",
    "shell_number_axis": "Numéro de Coquille",
    "shell_duration_seconds": "Durée de la coquille (secondes)",
    "peak_temp_y_axis": "Température Maximale (°C)",
    "glass_shell_journey_title": "Parcours de la Coquille en Verre dans le Temps",
    "multi_position_journey_title": "Parcours Multi-Position Coquille Verre (Capteur Tête)",
    
    # Shell analysis metrics
    "duration": "Durée",
    "avg_peak_temp": "Temp Pic Moy",
    "temp_range": "Plage Temp",
    "mean_peak_temp": "Temp Pic Moy",
    "temp_range_full": "Plage Temp",
    "head_max": "Max Tête",
    "avg_temperature": "Temp Moyenne",
    "temperature_stability": "Stabilité Temp",
    "shell_quality": "Qualité Coquille",
    "total_shells": "Total Coquilles",
    "avg_cycle_time": "Temps Cycle Moy",
    "production_rate": "Taux Production",
    "temp_max": "Temp Max (°C)",
    "temp_min": "Temp Min (°C)",
    "temp_avg": "Temp Moy (°C)",
    "duration": "Durée (s)",
    "samples": "Échantillons",
    "interactive_view": "Vue Température Interactive",
    "detailed_shell_analysis_title": "🔍 Analyse Détaillée - Coquille {shell_number}",
    "duration_metric": "Durée",
    "avg_temp_metric": "Temp Moyenne",
    "select_sensors": "Sélectionner Capteurs:",
    "total_shells_detected": "Total Coquilles Détectées",
    "avg_shell_duration": "Durée Coquille Moy",
    "total_samples": "Total Échantillons",
    "sensors": "Capteurs",
    "upload_multiple_files": "📁 Télécharger Plusieurs Fichiers de Position",
    "head_sensor_journey": "Comparaison du Parcours Thermique du Capteur Principal",
    "thermal_journey_insights": "📊 Aperçus du Parcours Thermique",
    "line_performance": "🎯 Évaluation des Performances de la Ligne",
    "ai_configuration": "🔑 Configuration IA",
    "report_type": "📊 Type de Rapport",
    "ai_analysis_report": "📋 Rapport d'Analyse IA",
    "interactive_shell_analysis": "🔍 Analyse Interactive des Coquilles",
    "download_options": "📥 Options de Téléchargement",
    "upload_journey_files": "📁 Télécharger Plusieurs Fichiers pour Rapport de Parcours",
    "report_template_generator": "📋 Générateur de Modèles de Rapport",
    "report_configuration": "⚙️ Configuration du Rapport",
    "report_customization": "🎨 Personnalisation du Rapport",
    "report_sections": "📑 Sections du Rapport",
    "data_selection": "📊 Sélection des Données",
    "live_preview": "👁️ Aperçu en Direct",
    "generate_download": "📥 Générer et Télécharger",
    
    # Main content
    "upload_prompt": "⬅︎    Placez ici votre/vos fichiers en format (.dat) pour commencer l'analyse thermique",
    "expected_format": "📋 Format de Données Attendu",
    "file_naming": "📁 Exemples:",
    "single_position": "Position unique:",
    "multiple_positions": "Positions multiples:",
    "analysis_capabilities": "🎯 Capacités d'Analyse:",
    "plateau_detection": "✅ Détection automatique des plateaux pour les coquilles en verre",
    "peak_extraction": "✅ Extraction des températures maximales",
    "production_rate": "✅ Calcul du taux de production (pièces/min)",
    "thermal_profiling": "✅ Profilage thermique multi-capteurs",
    "journey_reconstruction": "✅ Reconstruction du parcours entre positions",
    "adjust_thresholds_tip": "🔧 Astuce: Ajustez les seuils pour capturer les coques de verre",
    
    # AI section
    "ai_enhancement": "🤖 Amélioration par IA (Optionnel)",
    "enhance_with_ai": "🧠 Améliorer avec l'Analyse IA",
    "ai_help": "Utilisez l'IA pour générer des insights intelligents et des recommandations",
    "ai_key_required": "🔑 L'amélioration par IA nécessite une clé API OpenAI (configurer dans l'onglet Analyse IA)",
    "select_ai_sections": "Sélectionnez les sections améliorées par IA:",
    "ai_will_enhance": "✅ L'IA améliorera:",
    "upload_to_use": "📁 Veuillez télécharger des fichiers de données thermiques pour utiliser le Générateur de Modèles de Rapport",
    
    # Report sections
    "download_report": "📄 Télécharger le Rapport",
    "download_help": "Téléchargez votre rapport d'analyse thermique personnalisé",
    "generate_first": "Générez d'abord un rapport pour activer le téléchargement",
    "executive_summary": "Résumé Exécutif",
    "quality_assessment": "Évaluation de la Qualité",
    "recommendations": "Recommandations",
    "predictive_insights": "Perspectives Prédictives",

    # Analyse de Coquille
    "shell_analysis_title": "Analyse Coquille #{shell_number} - {position}",
    "shell_duration": "Durée: {duration}s",
    "select_shell_number": "Sélectionnez le numéro de la coquille:",
    "no_data_caption": "⚠️ Aucune donnée: {sensor}",
    "head_peak": "Pic de Tête",
    "peak": "Pic",
    "shell_duration_slider": "Durée approximative de la coquille (secondes)",
    "select_shell_help": "Choisissez la coquille à analyser en détail",
    "positions_analyzed": "Positions Analysées",
    "avg_max_temp": "Temp Max Moyenne",
    "temp_consistency": "Cohérence Température",
    "file": "Fichier",
    "temp_range_celsius": "Plage Temp (°C)",
    
    # Plateau Detection Interface
    "flatness_celsius": "Planéité (°C)",
    "plateau_min_seconds": "Plateau min (s)",
    "sensor_label": "Choisir Côté:",
    "no_plateau_found": "⚠️ Aucun plateau trouvé - essayez d'ajuster les seuils",
    "sensor_flatness_duration": "🔍 Capteur: {sensor} | Planéité: {flatness}°C | Durée min: {duration}s",
    "mobile_std_analysis": "📊 **Analyse d'Écart-Type Mobile**: Moy σ = {avg_std:.2f}°C, Max σ = {max_std:.2f}°C, Régions stables = {stable_percentage:.1f}%",
    "flatness_threshold": "Seuil de Planéité ({flatness}°C)",
    "temp_curves_with_std": "Courbes de Température avec Analyse d'Écart-Type Mobile - {position}",
    "mobile_std_celsius": "Écart-Type Mobile (°C)",
    "time_seconds": "Temps (secondes)",
    "temperature_celsius": "Température (°C)",
    
    # UI Messages and Status Texts
    "using_sheet": "📋 Utilisation de la feuille: '{sheet}' pour l'analyse",
    "error_reading_header": "⚠️ Erreur de lecture avec header=0, essai avec header=None: {error}",
    "time_column_identified": "⏰ Colonne de temps identifiée: '{column}'",
    "no_time_column": "⚠️ Aucune colonne de temps trouvée, création d'un temps séquentiel",
    "could_not_process_column": "⚠️ Impossible de traiter la colonne '{column}': {error}",
    "identified_sensors": "🌡️ Identifié {count} capteurs de température: {sensors}",
    "no_valid_columns": "❌ Aucune colonne de données numériques valides trouvée dans cette feuille!",
    "time_parsing_failed": "⚠️ Échec de l'analyse du temps ({error}), utilisation du timing séquentiel de secours",
    "error_processing_file": "Erreur lors du traitement de {filename}: {error}",
    "plateaus_found": "✅ **Trouvé {count} plateau(x)** qui répondent aux critères!",
    "no_sensor_data": "❌ Aucune donnée de capteur valide trouvée pour cette coquille. Veuillez vérifier vos données ou essayer un autre numéro de coquille.",
    "upload_multiple_files": "⚠️ Veuillez télécharger plusieurs fichiers de position pour l'analyse composite",
    "could_not_decode": "Impossible de décoder {filename}",
    "no_data_section": "Impossible de trouver la section de données dans {filename}",
    "no_data_found": "Aucune donnée trouvée dans {filename}",
    "no_valid_rows": "Aucune ligne de données valide dans {filename}",
    "excellent_consistency": "🎯 **Excellente Cohérence de Ligne**: La variation de température entre les positions est minimale",
    "moderate_variation": "⚠️ **Variation Modérée**: Certaines positions montrent des différences de température",
    "high_variation": "🚨 **Variation Élevée**: Différences de température significatives détectées entre les positions",
    "no_primary_sensor": "⚠️ Aucune donnée de capteur principal trouvée dans les fichiers téléchargés",
    "no_valid_data_extracted": "❌ Aucune donnée valide n'a pu être extraite des fichiers téléchargés",
    "provide_api_key": "⚠️ Veuillez fournir votre clé API OpenAI pour utiliser les fonctionnalités de rapport IA",
    "error_generating_report": "Erreur lors de la génération du rapport IA: {error}",
    "report_generated": "✅ Rapport généré avec succès!",
    "select_position_data": "⚠️ Veuillez sélectionner les données de position et vous assurer que tous les champs requis sont remplis",
    
    # UI Labels and Help Text
    "select_sheet": "📋 Sélectionner la feuille pour {filename}:",
    "choose_excel_sheet": "Choisissez quelle feuille Excel analyser",
    "column_info": "**Informations sur les Colonnes:**",
    "data_preview": "🔍 Aperçu des Données - {filename} ({sheet})",
    "auto_selected": "📍 Sélection automatique: {position}",
    "choose_shell": "Choisissez quelle coquille analyser en détail",
    "no_data_caption": "⚠️ Aucune donnée: {sensor}",
    "choose_position_ai": "Choisissez quelle position analyser avec l'IA",
    "click_shell_info": "Cliquez sur une coquille ci-dessous pour voir le profil thermique détaillé de cette région spécifique",
    "choose_shell_detail": "Choisissez une coquille spécifique à analyser en détail",
    "choose_report_scope": "Choisissez la portée de votre rapport d'analyse thermique",
    "choose_position_report": "Choisissez quelle position inclure dans le rapport",
    "data_preview_template": "**Aperçu des Données pour {position}:**",
    
    # File Upload Messages
    "upload_data_first_curves": "📁 Veuillez d'abord télécharger des fichiers de données pour commencer l'analyse des courbes de température.",
    "upload_data_first_shell": "📁 Veuillez d'abord télécharger des fichiers de données pour commencer l'analyse individuelle des coquilles.",
    "upload_data_first_peak": "📁 Veuillez d'abord télécharger des fichiers de données pour commencer l'analyse des températures maximales.",
    "upload_data_first_multi": "📁 Veuillez d'abord télécharger des fichiers de données pour commencer l'analyse multi-position.",
    "upload_data_first_interactive": "📁 Veuillez d'abord télécharger des fichiers de données pour commencer le tracé interactif.",
    "upload_dat_file": "📁 Veuillez d'abord télécharger un fichier .dat pour générer des rapports de position unique",
    
    # Processing Messages
    "processing_xlsx": "📊 Traitement du fichier XLSX: {filename}",
    "detected_sequential": "🕐 Données séquentielles détectées dans '{column}', traitement comme colonne de temps",
    "additional_numeric": "📊 Colonnes numériques supplémentaires: {columns}",
    "reconstructing_journey": "📍 Reconstruction du parcours de la coquille en verre à travers la ligne de trempe",
    
    # Interactive shell analysis
    "click_shell_info": "Cliquez sur une coquille ci-dessous pour voir le profil thermique détaillé de cette région spécifique",
    "select_shell_analysis": "Sélectionner une coquille pour analyse détaillée:",
    "choose_shell_detail": "Choisissez une coquille spécifique à analyser en détail",
    "shell_start": "Début Coquille",
    "shell_end": "Fin Coquille",
    
    # Report template generator
    "generate_professional_reports": "🎯 Générez des rapports d'analyse thermique professionnels sans écrire de prompts",
    "report_type": "📊 Type de Rapport",
    "output_format": "📄 Format de Sortie",
    "report_title_input": "📝 Titre du Rapport",
    "analyst_name_input": "👤 Nom de l'Analyste",
    "report_date_input": "📅 Date du Rapport",
    "company_department": "🏢 Entreprise/Département",
    "toggle_sections": "Activez/désactivez les sections que vous voulez inclure dans votre rapport:",
    "executive_summary_checkbox": "📋 Résumé Exécutif",
    "shell_detection_table": "🔍 Tableau de Détection des Coquilles",
    "temperature_profile": "🌡️ Profil de Température",
    "quality_alerts_checkbox": "⚠️ Alertes Qualité",
    "recommendations_checkbox": "💡 Recommandations",
    "charts_graphs": "📊 Graphiques et Diagrammes",
    
    # Report type options
    "single_position": "Position Unique",
    "full_line_journey": "Parcours Ligne Complète",
    "anomaly_summary_only": "Résumé d'Anomalies Seulement",
    "choose_report_scope": "Choisissez la portée de votre rapport d'analyse thermique",
    "select_download_format": "Sélectionnez le format de téléchargement pour votre rapport",
    "enter_custom_title": "Entrez un titre personnalisé pour votre rapport",
    "enter_analyst_name": "Entrez le nom de l'analyste",
    "select_report_date": "Sélectionnez la date de génération du rapport",
    "enter_company_dept": "Entrez le nom de l'entreprise ou du département",
    
    # Download buttons
    "download_as_txt": "📄 Télécharger en TXT",
    "download_data_csv": "📊 Télécharger Données (CSV)",
    "position_changes_detected": "🔄 Changements de Position Détectés: {count}",
    "position_change_number": "Changement de Position #",
    "timestamp_seconds": "Horodatage (s)",
    "min_temperature_celsius": "Température Min (°C)",
    "between_shells": "Entre Coquilles",
    "download_position_changes": "📥 Télécharger Changements de Position (CSV)",
    "position_changes_help": "Télécharger l'analyse des changements de position en fichier CSV"
}

# Load environment variables
load_dotenv()

# Initialize language in session state if not already set - MUST BE FIRST
if 'language' not in st.session_state:
    st.session_state['language'] = 'EN'

# Page configuration
st.set_page_config(
    page_title="Glass Toughening Analysis",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to get text based on current language
def get_text(key):
    lang = st.session_state['language']
    if lang == 'EN':
        return EN.get(key, key)
    elif lang == 'FR':
        return FR.get(key, key)
    return key

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
    }
    
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .metric-container {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
    
    /* Apple-style Control Panel */
    .apple-control-panel {
        background: rgba(28, 28, 30, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 16px;
        padding: 24px;
        margin: 16px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .apple-control-title {
        color: #ffffff;
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 8px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    .apple-control-subtitle {
        color: rgba(255, 255, 255, 0.6);
        font-size: 14px;
        margin-bottom: 24px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    /* Apple-style Select Boxes */
    .stSelectbox > div > div {
        background: rgba(58, 58, 60, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(10px) !important;
        color: #ffffff !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        font-size: 16px !important;
        padding: 12px 16px !important;
        transition: all 0.2s ease !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: rgba(10, 132, 255, 0.6) !important;
        box-shadow: 0 0 0 3px rgba(10, 132, 255, 0.1) !important;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #007AFF !important;
        box-shadow: 0 0 0 3px rgba(0, 122, 255, 0.2) !important;
    }
    
    .stSelectbox label {
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 16px !important;
        margin-bottom: 8px !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    }
    
    /* Apple-style dropdown arrow */
    .stSelectbox svg {
        color: rgba(255, 255, 255, 0.6) !important;
    }
    
    /* Apple-style sidebar */
    .css-1d391kg {
        background: rgba(28, 28, 30, 0.95) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    .css-1d391kg .stMarkdown {
        color: #ffffff !important;
    }
    
    /* Apple-style file uploader */
    .stFileUploader > div {
        background: rgba(58, 58, 60, 0.8) !important;
        border: 2px dashed rgba(255, 255, 255, 0.3) !important;
        border-radius: 12px !important;
        padding: 24px !important;
        transition: all 0.2s ease !important;
    }
    
    .stFileUploader > div:hover {
        border-color: rgba(10, 132, 255, 0.6) !important;
        background: rgba(58, 58, 60, 0.9) !important;
    }
    
    .stFileUploader label {
        color: #ffffff !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    }
    
    /* Apple-style divider */
    hr {
        border: none !important;
        height: 1px !important;
        background: rgba(255, 255, 255, 0.1) !important;
        margin: 16px 0 !important;
    }
</style>
""", unsafe_allow_html=True)

def collect_ui_metadata(plant, line_number, glass_shell, campaign_number, file_date, line_speed, temperature_u4, toughening_positions, air_pressure_top, air_pressure_bottom, air_temperature, rotation_speed):
    """Collect metadata from UI fields in Global Identification and Toughening Parameters"""
    print("[DEBUG] Starting collect_ui_metadata function")
    metadata = {}

    try:
        # Global Identification fields
        print("[DEBUG] Collecting Global Identification fields")
        metadata['plant'] = plant or ''
        metadata['line_number'] = line_number or ''
        metadata['glass_shell'] = glass_shell or ''
        metadata['campaign_number'] = campaign_number or ''
        metadata['date'] = file_date or date.today()
        print(f"[DEBUG] Global fields collected: {metadata}")

        # Toughening Parameters fields - Correct mapping based on PDF generation table
        print("[DEBUG] Collecting Toughening Parameters fields")
        # PDF expects: 'Line speed (pcs/min)' -> metadata.get('heating_temp')
        metadata['heating_temp'] = line_speed or ''  # Line speed maps to heating_temp for PDF
        # PDF expects: 'Temperature U4 furnace (°C)' -> metadata.get('heating_time')
        metadata['heating_time'] = temperature_u4 or ''  # Temperature U4 maps to heating_time for PDF
        # PDF expects: 'Number of toughening positions' -> metadata.get('toughening_positions')
        metadata['toughening_positions'] = toughening_positions or ''  # Direct mapping
        # Store both pressure values separately as requested by Antoine
        metadata['air_pressure_top'] = air_pressure_top or ''  # GS Top
        metadata['air_pressure_bottom'] = air_pressure_bottom or ''  # GS Bottom
        # PDF expects: 'Air temperature (°C)' -> metadata.get('quench_time')
        metadata['quench_time'] = air_temperature or ''  # Air temperature maps to quench_time for PDF
        # PDF expects: 'Rotation speed (% / rpm)' -> metadata.get('rotation_speed')
        metadata['rotation_speed'] = rotation_speed or ''  # Direct mapping
        print(f"[DEBUG] All metadata collected successfully: {metadata}")
        
        return metadata
    except Exception as e:
        print(f"[ERROR] Error in collect_ui_metadata: {str(e)}")
        print(f"[ERROR] Error type: {type(e).__name__}")
        raise e

# Shell summary functionality removed for cleaner interface

# Consolidated shell data functionality removed for cleaner interface

def generate_insight_briefing_pdf(metadata, cooling_curve_data, consolidated_shell_data, position_data=None):
    """Generate multi-page Insight Briefing PDF with metadata, cooling curve, and shell data"""
    print("[DEBUG] Starting generate_insight_briefing_pdf function")
    print(f"[DEBUG] Metadata: {metadata}")
    print(f"[DEBUG] Cooling curve data: {cooling_curve_data}")
    print(f"[DEBUG] Consolidated shell data count: {len(consolidated_shell_data)}")
    
    try:
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)
        print("[DEBUG] PDF document created successfully")
        
        # Get styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=HexColor('#1f4e79')
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=12,
            textColor=HexColor('#1f4e79')
        )
        
        story = []
        
        # PAGE 1: INSIGHT PAGE
        story.append(Paragraph("SEDIVER Insight Briefing", title_style))
        story.append(Spacer(1, 20))
        
        # Metadata section
        story.append(Paragraph("Global Identification", heading_style))
        
        metadata_data = [
            ['Plant:', str(metadata.get('plant', 'N/A'))],
            ['Line #:', str(metadata.get('line_number', 'N/A'))],
            ['Glass Shell:', str(metadata.get('glass_shell', 'N/A'))],
            ['Campaign #:', str(metadata.get('campaign_number', 'N/A'))],
            ['Date:', str(metadata.get('date', 'N/A'))]
        ]
        
        metadata_table = Table(metadata_data, colWidths=[2*inch, 3*inch])
        metadata_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), HexColor('#f0f0f0')),
            ('TEXTCOLOR', (0, 0), (-1, -1), black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, black)
        ]))
        
        story.append(metadata_table)
        story.append(Spacer(1, 20))
        
        # Toughening Parameters
        story.append(Paragraph("Toughening Parameters", heading_style))
        
        toughening_data = [
            ['Line speed (pcs/min):', str(metadata.get('heating_temp', 'N/A'))],
            ['Temperature U4 furnace (°C):', str(metadata.get('heating_time', 'N/A'))],
            ['Number of toughening positions with air / open positions:', str(metadata.get('toughening_positions', 'N/A'))],
            ['GS Top (bar):', str(metadata.get('air_pressure_top', 'N/A'))],
            ['GS Bottom (bar):', str(metadata.get('air_pressure_bottom', 'N/A'))],
            ['Air temperature (°C):', str(metadata.get('quench_time', 'N/A'))],
            ['Rotation speed (% / rpm):', str(metadata.get('rotation_speed', 'N/A'))]
        ]
        
        toughening_table = Table(toughening_data, colWidths=[2*inch, 3*inch])
        toughening_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), HexColor('#f0f0f0')),
            ('TEXTCOLOR', (0, 0), (-1, -1), black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, black)
        ]))
        
        story.append(toughening_table)
        story.append(Spacer(1, 30))
        
        # Position-specific averages section
        if position_data:
            story.append(Paragraph("Position Temperature Averages", heading_style))
            
            # Create position averages data
            position_averages = []
            # Keep original sensor names from .dat file

            for pos_name, pos_info in position_data.items():
                df = pos_info['data']
                available_sensors = [col for col in df.columns if col not in ['Time', 'Time_seconds', 'Head', 'Unnamed: 6']]
                if available_sensors:
                    sensor_to_use = available_sensors[0]
                    display_name = sensor_to_use  # Use original name
                    avg_temp = df[sensor_to_use].mean()
                    max_temp = df[sensor_to_use].max()
                    min_temp = df[sensor_to_use].min()
                    
                    position_averages.append([
                        f"{pos_name} ({display_name}):",
                        f"Avg: {avg_temp:.1f}°C, Range: {min_temp:.1f}-{max_temp:.1f}°C"
                    ])
            
            if position_averages:
                position_table = Table(position_averages, colWidths=[2*inch, 3*inch])
                position_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (0, -1), HexColor('#f0f0f0')),
                    ('TEXTCOLOR', (0, 0), (-1, -1), black),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                    ('GRID', (0, 0), (-1, -1), 1, black)
                ]))
                story.append(position_table)
            else:
                story.append(Paragraph("No position data available for analysis.", styles['Normal']))
        else:
            story.append(Paragraph("No position data available for analysis.", styles['Normal']))
        
        story.append(Spacer(1, 30))
        
        # Cooling Curve Chart
        story.append(Paragraph("Cooling Curve Analysis", heading_style))
        story.append(Paragraph("Shell summary data not available - analysis focused on metadata only.", styles['Normal']))
        
        # PAGE 2: DATA APPENDIX
        story.append(PageBreak())
        story.append(Paragraph("Data Appendix", title_style))
        story.append(Spacer(1, 20))
        story.append(Paragraph("Shell summary data removed for cleaner interface.", styles['Normal']))
        
        # Build PDF
        print("[DEBUG] Building PDF document")
        doc.build(story)
        buffer.seek(0)
        print("[DEBUG] PDF generation completed successfully")
        return buffer
    except Exception as e:
        print(f"[ERROR] Error in generate_insight_briefing_pdf: {str(e)}")
        print(f"[ERROR] Error type: {type(e).__name__}")
        raise e

def generate_pdf_report(plateaus, df, fig, report_title="Thermal Analysis Report", 
                       analyst_name="Sediver Analyst", include_sections=None, 
                       pdf_type="full", add_watermark=False):
    """Generate PDF report with SEDIVER branding using reportlab"""
    
    if include_sections is None:
        include_sections = {
            'executive_summary': True,
            'shell_detection': True,
            'temperature_charts': True,
            'quality_alerts': True,
            'recommendations': True
        }
    
    # Create PDF buffer
    buffer = BytesIO()
    
    # Custom page template with watermark
    if add_watermark:
        from reportlab.platypus import PageTemplate, Frame
        from reportlab.lib.pagesizes import A4 as PAGE_A4
        
        class WatermarkPageTemplate(PageTemplate):
            def __init__(self, id, frames, pagesize=PAGE_A4):
                PageTemplate.__init__(self, id, frames, pagesize)
                
            def beforeDrawPage(self, canvas, doc):
                from reportlab.lib import colors as rl_colors
                canvas.saveState()
                canvas.setFillAlpha(0.15)
                canvas.setFillColor(gray)
                canvas.setFont("Helvetica-Bold", 48)
                
                # Calculate center position and rotate
                width, height = PAGE_A4
                canvas.translate(width/2, height/2)
                canvas.rotate(45)
                canvas.drawCentredText(0, 0, "INTERNAL USE ONLY")
                canvas.restoreState()
        
        # Create document with watermark template
        frame = Frame(72, 18, PAGE_A4[0]-144, PAGE_A4[1]-90, leftPadding=0, bottomPadding=0, rightPadding=0, topPadding=0)
        watermark_template = WatermarkPageTemplate('watermark', [frame])
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, 
                               topMargin=72, bottomMargin=18)
        doc.addPageTemplates([watermark_template])
    else:
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, 
                               topMargin=72, bottomMargin=18)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Modern color palette
    from reportlab.lib.colors import Color
    sediver_blue = Color(0, 85/255, 184/255)  # SEDIVER blue #0055B8
    modern_gray = Color(0.15, 0.15, 0.15)     # Dark gray for text
    light_gray = Color(0.95, 0.95, 0.95)     # Light gray for backgrounds
    accent_blue = Color(0.2, 0.4, 0.8)       # Lighter blue for accents
    
    # Modern title style with clean typography
    title_style = ParagraphStyle(
        'ModernTitle',
        parent=styles['Heading1'],
        fontSize=32,
        spaceAfter=20,
        spaceBefore=10,
        alignment=TA_CENTER,
        textColor=sediver_blue,
        fontName='Helvetica-Bold',
        leading=36
    )
    
    # Clean subtitle style
    subtitle_style = ParagraphStyle(
        'ModernSubtitle',
        parent=styles['Title'],
        fontSize=18,
        spaceAfter=30,
        spaceBefore=10,
        alignment=TA_CENTER,
        textColor=modern_gray,
        fontName='Helvetica',
        leading=22
    )
    
    # Modern heading style with subtle spacing
    heading_style = ParagraphStyle(
        'ModernHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=8,
        spaceBefore=18,
        textColor=sediver_blue,
        fontName='Helvetica-Bold',
        borderWidth=0,
        borderPadding=0,
        leftIndent=0,
        leading=20
    )
    
    # Clean body text style
    body_style = ParagraphStyle(
        'ModernBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        textColor=modern_gray,
        fontName='Helvetica',
        leading=14,
        leftIndent=0
    )
    
    # Accent style for key information
    accent_style = ParagraphStyle(
        'AccentText',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        textColor=accent_blue,
        fontName='Helvetica-Bold',
        leading=15
    )
    
    # Story (content) list
    story = []
    
    # Modern cover page design
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("SEDIVER", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(report_title, subtitle_style))
    story.append(Spacer(1, 0.8*inch))
    
    # Get current date
    today = datetime.now().strftime("%B %d, %Y")
    
    # Modern metadata section with clean styling
    metadata_style = ParagraphStyle(
        'Metadata',
        parent=body_style,
        fontSize=11,
        alignment=TA_CENTER,
        textColor=modern_gray,
        spaceAfter=4
    )
    
    story.append(Paragraph(f"<b>Analyst:</b> {analyst_name}", metadata_style))
    story.append(Paragraph(f"<b>Date:</b> {today}", metadata_style))
    story.append(Spacer(1, 0.4*inch))
    
    # Confidential notice with modern styling
    confidential_style = ParagraphStyle(
        'Confidential',
        parent=styles['Italic'],
        fontSize=9,
        alignment=TA_CENTER,
        textColor=Color(0.5, 0.5, 0.5),
        spaceAfter=4
    )
    story.append(Paragraph("SEDIVER R&D - CONFIDENTIAL", confidential_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Executive Summary with modern styling
    if include_sections.get('executive_summary', True):
        story.append(Paragraph("Executive Summary", heading_style))
        
        total_duration = df['Time_seconds'].max() if not df.empty else 0
        shell_count = len(plateaus) if plateaus else 0
        
        # Modern summary card design
        summary_text = f"""
        <b style="color: #0055B8;">Key Findings:</b> Duration: <b>{total_duration:.1f}s</b> | Shells: <b>{shell_count}</b> | Method: Dynamic plateau detection | Quality: <b>{"Good" if not df.empty else "No data"}</b>
        """
        story.append(Paragraph(summary_text, accent_style))
        story.append(Spacer(1, 0.2*inch))
    
    # Shell Detection Table
    if include_sections.get('shell_detection', True):
        story.append(Paragraph("Shell Detection Results", heading_style))
        
        if plateaus:
            # Create table data with detected shells
            table_data = [['Shell #', 'Start (s)', 'End (s)', 'Duration (s)', 'Avg Temp (°C)', 'Peak Temp (°C)', 'Stability']]
            
            for i, plateau in enumerate(plateaus, 1):
                start_time = plateau['start_time']
                end_time = plateau['end_time']
                duration = end_time - start_time
                
                # Get temperature data for this plateau
                plateau_data = df[(df['Time_seconds'] >= start_time) & (df['Time_seconds'] <= end_time)]
                if not plateau_data.empty:
                    temp_cols = [col for col in plateau_data.columns if col not in ['Time', 'Time_seconds', 'Unnamed: 6']]
                    if temp_cols:
                        avg_temp = plateau_data[temp_cols].mean().mean()
                        peak_temp = plateau_data[temp_cols].max().max()
                    else:
                        avg_temp = peak_temp = 0
                else:
                    avg_temp = peak_temp = 0
                
                stability = "Good" if duration > 5 else "Short"
                
                table_data.append([
                    str(i),
                    f'{start_time:.1f}',
                    f'{end_time:.1f}',
                    f'{duration:.1f}',
                    f'{avg_temp:.1f}',
                    f'{peak_temp:.1f}',
                    stability
                ])
        else:
            # Create placeholder table when no shells detected
            table_data = [
                ['Shell #', 'Start (s)', 'End (s)', 'Duration (s)', 'Avg Temp (°C)', 'Peak Temp (°C)', 'Stability'],
                ['—', '— None detected —', '—', '—', '—', '—', '—']
            ]
        
        # Modern table design
        table = Table(table_data)
        from reportlab.lib import colors as rl_colors
        
        # Modern table styling with clean design
        table.setStyle(TableStyle([
            # Header styling - modern blue gradient effect
            ('BACKGROUND', (0, 0), (-1, 0), sediver_blue),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            
            # Modern padding and spacing
            ('TOPPADDING', (0, 0), (-1, 0), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            
            # Clean alternating row colors
            ('BACKGROUND', (0, 1), (-1, -1), light_gray),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, light_gray]),
            
            # Subtle grid lines
            ('GRID', (0, 0), (-1, -1), 0.5, Color(0.8, 0.8, 0.8)),
            ('LINEBELOW', (0, 0), (-1, 0), 2, sediver_blue),
        ]))
        
        story.append(table)
        story.append(Spacer(1, 0.2*inch))
    
    # Temperature Profile Charts (Compact)
    if include_sections.get('temperature_charts', True) and fig:
        story.append(Paragraph("Temperature Profile Analysis", heading_style))
        
        try:
            import tempfile
            import os
            import time
            
            # Create temporary file in a more controlled way
            temp_dir = tempfile.gettempdir()
            tmp_png = os.path.join(temp_dir, f"chart_{int(time.time() * 1000)}.png")
            
            # Write image to temporary file using kaleido engine
            fig.write_image(tmp_png, format="png", width=600, height=350, scale=2, engine="kaleido")
            
            # Wait a moment to ensure file is fully written
            time.sleep(0.1)
            
            # Verify file was created and has content
            if os.path.exists(tmp_png) and os.path.getsize(tmp_png) > 1000:  # Ensure meaningful file size
                # Read the file into memory first
                with open(tmp_png, 'rb') as f:
                    img_data = f.read()
                
                # Create BytesIO from the file data
                img_buffer = BytesIO(img_data)
                
                # Add image to PDF using BytesIO
                img = RLImage(img_buffer, width=4.5*inch, height=2.6*inch)
                story.append(img)
            else:
                story.append(Paragraph("Chart image could not be generated - file verification failed", body_style))
            
            # Clean up temporary file
            try:
                if os.path.exists(tmp_png):
                    os.unlink(tmp_png)
            except:
                pass
                    
        except Exception as e:
            story.append(Paragraph(f"Chart generation failed: {str(e)}", body_style))
        
        story.append(Spacer(1, 0.15*inch))
    
    # Quality Alerts with modern design
    if include_sections.get('quality_alerts', True):
        story.append(Paragraph("Quality Alerts &amp; Recommendations", heading_style))
        
        alerts = []
        if plateaus:
            # Check for short plateaus
            short_plateaus = [p for p in plateaus if (p['end_time'] - p['start_time']) < 3]
            if short_plateaus:
                alerts.append(f"⚠️ {len(short_plateaus)} short plateau(s) detected")
            
            # Check for temperature variations
            if not df.empty:
                temp_cols = [col for col in df.columns if col not in ['Time', 'Time_seconds', 'Unnamed: 6']]
                if temp_cols and len(temp_cols) > 1:
                    temp_std = df[temp_cols].std(axis=1).mean()
                    if temp_std > 10:
                        alerts.append(f"⚠️ High temp variation (σ = {temp_std:.1f}°C)")
        
        if not alerts:
            alerts.append("✅ No quality issues detected")
        
        # Modern recommendations with clean bullet points
        recommendations = [
            "• Monitor plateau consistency for optimal process control",
            "• Investigate temperature variations exceeding ±5°C threshold", 
            "• Maintain regular sensor calibration schedule"
        ]
        
        # Style alerts and recommendations differently
        alert_style = ParagraphStyle(
            'AlertStyle',
            parent=body_style,
            fontSize=10,
            textColor=Color(0.8, 0.4, 0.1) if alerts and "⚠️" in alerts[0] else Color(0.1, 0.6, 0.1),
            spaceAfter=4
        )
        
        rec_style = ParagraphStyle(
            'RecommendationStyle',
            parent=body_style,
            fontSize=10,
            textColor=modern_gray,
            spaceAfter=3,
            leftIndent=10
        )
        
        # Add alerts
        for alert in alerts:
            story.append(Paragraph(alert, alert_style))
        
        story.append(Spacer(1, 0.1*inch))
        
        # Add recommendations
        for rec in recommendations:
            story.append(Paragraph(rec, rec_style))
        
        story.append(Spacer(1, 0.15*inch))
    # Build PDF
    doc.build(story)
    
    # Get PDF bytes
    pdf_bytes = buffer.getvalue()
    buffer.close()
    
    return pdf_bytes

# Header
st.markdown(f'<h1 class="main-header">{get_text("app_title")}</h1>', unsafe_allow_html=True)

# Sidebar - Apple-style Control Panel
st.sidebar.markdown(f"""
<div class="apple-control-panel">
    <div class="apple-control-title">{get_text("control_panel")}</div>
    <div class="apple-control-subtitle">{get_text("control_subtitle")}</div>
</div>
""", unsafe_allow_html=True)

# File Upload Section in Control Panel
st.sidebar.markdown(f"""
<div style="margin: 16px 0;">
    <div style="color: #ffffff; font-size: 16px; font-weight: 500; margin-bottom: 8px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        {get_text("data_files")}
    </div>
</div>
""", unsafe_allow_html=True)

# File upload for toughening data in sidebar
uploaded_files = st.sidebar.file_uploader(
    get_text("upload_files"),
    type=["dat", "xlsx", "csv", "txt"],
    accept_multiple_files=True,
    help=get_text("upload_help"),
    label_visibility="collapsed"
)

# Add a subtle divider
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Main Controls in Sidebar - Always visible


# Initialize position_data if not exists
if 'position_data' not in locals():
    position_data = {}

# Define analysis_type as a placeholder since the selectbox was removed
analysis_type = "all_sections"

# Language selector at the bottom of sidebar
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

language_options = {"EN": "English", "FR": "Français"}
selected_lang = st.sidebar.selectbox(
    "Language / Langue",  # Fixed label to avoid circular dependency
    options=list(language_options.keys()),
    format_func=lambda x: language_options[x],
    key="language_selector",
    index=0 if st.session_state['language'] == 'EN' else 1
)

# Update language in session state when changed
if selected_lang != st.session_state['language']:
    st.session_state['language'] = selected_lang
    st.rerun()  # Direct rerun instead of calling change_language function

if uploaded_files:
    # Cache hygiene - clear stale data on new file upload
    st.session_state.pop("detected_shells", None)
    
    # Process uploaded files
    position_data = {}
    
    for uploaded_file in uploaded_files:
        try:
            # Extract position from filename
            filename = uploaded_file.name
            position_match = filename.split('_')[-1].split('.')[0] if '_' in filename else filename.split('.')[0]
            position_name = get_text("position_with_match").format(match=position_match)
            
            # Handle different file formats
            if filename.endswith('.xlsx'):
                # XLSX Multi-sheet processing
                st.info(get_text("processing_xlsx").format(filename=filename))
                
                # Read all sheets
                excel_file = pd.ExcelFile(uploaded_file)
                sheet_names = excel_file.sheet_names
                
                st.write(f"🔍 Found {len(sheet_names)} sheets: {', '.join(sheet_names)}")
                
                # Smart sheet selection with user override
                main_sheet = None
                sheet_priorities = ['temperature', 'temp', 'data', 'main', 'recap', 'thermal', 'sensor']
                
                # Find best matching sheet
                for priority in sheet_priorities:
                    for sheet in sheet_names:
                        if priority in sheet.lower():
                            main_sheet = sheet
                            break
                    if main_sheet:
                        break
                
                if not main_sheet:
                    main_sheet = sheet_names[0]  # Default to first sheet
                
                # Allow user to select different sheet if multiple exist
                if len(sheet_names) > 1:
                    selected_sheet = st.selectbox(
                        f"📋 Select sheet for {filename}:",
                        sheet_names,
                        index=sheet_names.index(main_sheet),
                        key=f"sheet_select_{filename}",
                        help="Choose which Excel sheet to analyze"
                    )
                    main_sheet = selected_sheet
                
                st.success(get_text("using_sheet").format(sheet=main_sheet))
                
                # Read the selected sheet with enhanced error handling
                try:
                    df = pd.read_excel(uploaded_file, sheet_name=main_sheet, header=0)
                except Exception as e:
                    st.warning(get_text("error_reading_header").format(error=e))
                    df = pd.read_excel(uploaded_file, sheet_name=main_sheet, header=None)
                    # Use first row as column names if it looks like headers
                    if df.iloc[0].dtype == 'object':
                        df.columns = df.iloc[0]
                        df = df.drop(df.index[0]).reset_index(drop=True)
                
                # Smart column detection for XLSX
                st.write(f"📊 Sheet contains {df.shape[0]} rows and {df.shape[1]} columns")
                
                # Show data preview
                with st.expander(f"🔍 Data Preview - {filename} ({main_sheet})"):
                    st.write("**First 5 rows:**")
                    st.dataframe(df.head(), use_container_width=True)
                    st.write("**Column Info:**")
                    col_info = []
                    for col in df.columns:
                        non_null = df[col].notna().sum()
                        data_type = str(df[col].dtype)
                        sample_val = str(df[col].dropna().iloc[0]) if non_null > 0 else "N/A"
                        col_info.append({
                            "Column": col,
                            "Type": data_type,
                            "Non-null": f"{non_null}/{len(df)}",
                            "Sample": sample_val[:50] + "..." if len(sample_val) > 50 else sample_val
                        })
                    st.dataframe(pd.DataFrame(col_info), use_container_width=True)
                
                st.write(f"🏷️ Columns detected: {list(df.columns)}")
                
                # Enhanced time column detection
                time_col = None
                time_keywords = ['time', 'temps', 'duration', 'timestamp', 'elapsed', 'seconds', 'minutes', 'hours']
                
                # First, look for exact matches
                for col in df.columns:
                    col_lower = str(col).lower().strip()
                    if col_lower in time_keywords:
                        time_col = col
                        break
                
                # If no exact match, look for partial matches
                if not time_col:
                    for col in df.columns:
                        col_lower = str(col).lower().strip()
                        if any(keyword in col_lower for keyword in time_keywords):
                            time_col = col
                            break
                
                # If still no time column, check if first column looks like time
                if not time_col and len(df.columns) > 0:
                    first_col = df.columns[0]
                    # Check if first column has sequential or time-like data
                    try:
                        first_col_data = pd.to_numeric(df[first_col], errors='coerce')
                        if first_col_data.notna().sum() > len(df) * 0.8:  # 80% numeric
                            # Check if it's sequential (likely time)
                            diff = first_col_data.diff().dropna()
                            if diff.std() < diff.mean() * 0.1:  # Low variance in differences
                                time_col = first_col
                                st.info(get_text("detected_sequential").format(column=first_col))
                    except:
                        pass
                
                if time_col:
                    st.success(get_text("time_column_identified").format(column=time_col))
                    # Convert time to seconds if needed
                    if df[time_col].dtype == 'object':
                        try:
                            # Try to parse as time format
                            df['Time_seconds'] = pd.to_timedelta(df[time_col]).dt.total_seconds()
                        except:
                            # Create sequential time
                            df['Time_seconds'] = df.index * 0.1  # Assume 0.1s resolution
                    else:
                        df['Time_seconds'] = df[time_col]
                        
                    # Rename original time column for consistency
                    df = df.rename(columns={time_col: 'Time'})
                else:
                    st.warning(get_text("no_time_column"))
                    df['Time_seconds'] = df.index * 0.1
                    df['Time'] = df['Time_seconds']
                
                # Enhanced numeric column processing
                numeric_columns = []
                temperature_columns = []
                
                for col in df.columns:
                    if col not in ['Time', 'Time_seconds', 'Unnamed: 6']:
                        # Try to convert to numeric
                        try:
                            original_col = df[col].copy()
                            
                            # Handle various decimal separators and formats
                            if df[col].dtype == 'object':
                                # Clean string data
                                df[col] = df[col].astype(str).str.replace(',', '.')
                                df[col] = df[col].str.replace(' ', '')  # Remove spaces
                                df[col] = df[col].str.replace('°C', '')  # Remove temperature units
                                df[col] = df[col].str.replace('°', '')   # Remove degree symbols
                            
                            # Convert to numeric
                            df[col] = pd.to_numeric(df[col], errors='coerce')
                            
                            # Validate if this is a temperature sensor
                            valid_data = df[col].dropna()
                            if len(valid_data) > 0:
                                data_range = valid_data.max() - valid_data.min()
                                mean_val = valid_data.mean()
                                
                                # Temperature validation criteria
                                is_temperature = (
                                    len(valid_data) > len(df) * 0.1 and  # At least 10% valid data
                                    data_range > 5 and                    # Reasonable temperature range
                                    mean_val > -50 and mean_val < 2000    # Realistic temperature bounds
                                )
                                
                                if is_temperature:
                                    numeric_columns.append(col)
                                    
                                    # Check if it's likely a temperature sensor
                                    col_name_lower = str(col).lower()
                                    if any(temp_word in col_name_lower for temp_word in 
                                          ['temp', 'temperature', 'sensor', 'tc', 'thermocouple', '°c']):
                                        temperature_columns.append(col)
                                    elif mean_val > 20 and mean_val < 1500:  # Typical industrial temperature range
                                        temperature_columns.append(col)
                                else:
                                    # Restore original if not temperature data
                                    df[col] = original_col
                                    
                        except Exception as e:
                            # Restore original column if processing fails
                            df[col] = original_col
                            st.warning(get_text("could_not_process_column").format(column=col, error=e))
                
                # Keep only relevant columns
                final_columns = ['Time', 'Time_seconds'] + numeric_columns
                df = df[final_columns]
                
                # Report findings
                if temperature_columns:
                    st.success(get_text("identified_sensors").format(count=len(temperature_columns), sensors=temperature_columns))
                if numeric_columns and not temperature_columns:
                    st.info(f"📊 Processed {len(numeric_columns)} numeric columns: {numeric_columns}")
                elif len(numeric_columns) > len(temperature_columns):
                    other_numeric = [col for col in numeric_columns if col not in temperature_columns]
                    st.info(get_text("additional_numeric").format(columns=other_numeric))
                
                if not numeric_columns:
                    st.error(get_text("no_valid_columns"))
                    continue
                
                # Extract position from filename for XLSX
                if 'position' in filename.lower():
                    pos_match = filename.lower().split('position')[-1].split('.')[0]
                    position_name = get_text("position_with_match").format(match=pos_match)
                elif any(char.isdigit() for char in filename):
                    # Extract numbers from filename
                    import re
                    numbers = re.findall(r'\d+', filename)
                    if numbers:
                        position_name = get_text("position_number").format(number=numbers[0])
                else:
                    # Use filename without extension as position name
                    position_name = filename.split('.')[0]
                
                # Store processed XLSX data
                position_data[position_name] = {
                    'data': df,
                    'header': {'sheet_name': main_sheet, 'total_sheets': len(sheet_names)},
                    'filename': filename,
                    'file_type': 'xlsx',
                    'temperature_sensors': temperature_columns,
                    'all_numeric_columns': numeric_columns
                }
                
            else:
                # Original .dat file processing
                # Read file with encoding handling
                content = None
                encodings_to_try = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
                
                for encoding in encodings_to_try:
                    try:
                        uploaded_file.seek(0)
                        content = uploaded_file.read().decode(encoding)
                        break
                    except UnicodeDecodeError:
                        continue
                
                if content is None:
                    uploaded_file.seek(0)
                    content = uploaded_file.read().decode('utf-8', errors='replace')
                
                # Parse Connect DataFile format
                if '[Connect DataFile]' in content:
                    lines = content.split('\n')
                    
                    # Parse header
                    header_info = {}
                    data_start_line = 0
                    
                    for i, line in enumerate(lines):
                        if line.startswith('[Connect DataFile]'):
                            continue
                        elif ':;' in line and not line.startswith('Time;'):
                            key, value = line.split(':;', 1)
                            header_info[key] = value
                        elif line.startswith('Time;'):
                            data_start_line = i
                            break
                    
                    # Read data
                    data_lines = lines[data_start_line:]
                    data_content = '\n'.join(data_lines)
                    
                    df = pd.read_csv(StringIO(data_content), sep=';')
                    
                    # Clean and convert numeric columns
                    numeric_columns = [col for col in df.columns if col != 'Time']
                    for col in numeric_columns:
                        if col in df.columns:
                            # Replace commas with dots for decimal numbers
                            df[col] = df[col].astype(str).str.replace(',', '.')
                            # Convert to numeric, handling any remaining issues
                            df[col] = pd.to_numeric(df[col], errors='coerce')
                    
                    # Convert time to seconds using robust Euro-Time Parser
                    if 'Time' in df.columns:
                        def euro_to_seconds(t: str) -> float:
                            """
                            Convert European time format "hh:mm:ss,ms" to seconds
                            Expects format like "00:00:00,150" or "00:01:09,350"
                            """
                            try:
                                # Handle string conversion and strip whitespace
                                t = str(t).strip()
                                
                                # Split by colon to get hours, minutes, and seconds+milliseconds
                                h, m, rest = t.split(":")
                                
                                # Split seconds and milliseconds by comma
                                s, ms = rest.split(",")
                                
                                # Convert to total seconds
                                return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
                            except (ValueError, AttributeError, IndexError) as e:
                                # Fallback for malformed time strings
                                return 0.0
                        
                        try:
                            # Apply Euro-Time Parser to convert time column
                            df['Time_seconds'] = df['Time'].apply(euro_to_seconds)
                            
                            # Verify conversion worked by checking if we have reasonable time values
                            if df['Time_seconds'].max() == 0 or df['Time_seconds'].isna().all():
                                raise ValueError("Euro-Time Parser failed - all values are 0 or NaN")
                                
                        except Exception as e:
                            # Fallback: create sequential time based on row index and resolution
                            st.warning(get_text("time_parsing_failed").format(error=str(e)))
                            resolution = float(header_info.get('Resolution', '0.05').replace(',', '.'))
                            df['Time_seconds'] = df.index * resolution
                else:
                    # Handle other formats (CSV, etc.)
                    uploaded_file.seek(0)
                    df = pd.read_csv(uploaded_file)
                    
                    # Basic time handling for CSV
                    if 'Time_seconds' not in df.columns:
                        df['Time_seconds'] = df.index * 0.1
                    if 'Time' not in df.columns:
                        df['Time'] = df['Time_seconds']
                
                # Extract and parse date from header_info
                if 'Date' in header_info:
                    try:
                        # Parse date string (format: DD/MM/YYYY)
                        date_str = header_info['Date'].strip()
                        parsed_date = datetime.strptime(date_str, "%d/%m/%Y").date()
                        st.session_state.file_date = parsed_date
                    except (ValueError, AttributeError) as e:
                        # Fallback to today's date if parsing fails
                        st.session_state.file_date = date.today()
                else:
                    # Default to today's date if no date in header
                    st.session_state.file_date = date.today()
                
                position_data[position_name] = {
                    'data': df,
                    'header': header_info,
                    'filename': filename
                }
                
        except Exception as e:
            st.error(get_text("error_processing_file").format(filename=uploaded_file.name, error=str(e)))
    
    if position_data:
        # Display loaded positions
        cols = st.columns(min(len(position_data), 4))
        for i, (pos_name, pos_info) in enumerate(position_data.items()):
            with cols[i % 4]:
                # Handle different file types
                file_type = pos_info.get('file_type', 'dat')
                
                if file_type == 'xlsx':
                    # XLSX file display
                    sheet_info = pos_info['header'].get('sheet_name', 'Unknown')
                    total_sheets = pos_info['header'].get('total_sheets', 1)
                    temp_sensors = len(pos_info.get('temperature_sensors', []))
                    
                    st.caption(f"Sheet: {sheet_info} ({total_sheets} total)")
                else:
                    # DAT file display (original) - metrics removed for cleaner interface
                    st.markdown("---")
        
        # Position Selection - Show after data is loaded
        if position_data:
            if len(position_data) == 1:
                # Auto-select if only one position
                selected_position = list(position_data.keys())[0]
                st.sidebar.info(f"📍 Auto-selected: {selected_position}")
            else:
                # Show dropdown for multiple positions
                selected_position = st.sidebar.selectbox(
                    get_text("select_position"), 
                    list(position_data.keys()),
                    key="main_position_select",
                    help=get_text("select_position")
                )
        else:
            st.sidebar.selectbox(
                get_text("select_position"), 
                [get_text("upload_more")],
                disabled=True,
                key="main_position_select_disabled",
                help=get_text("position_help")
            )
            selected_position = None

        # Use analysis type and position from sidebar controls
        if True:
            with st.expander(get_text("temp_curves_header"), expanded=True):
                
                if not selected_position:
                    st.info(get_text("upload_data_first_curves"))
                    st.markdown("""
                    **This analysis will provide:**
                    - 📊 Comprehensive data summary with sample count, duration, and temperature ranges
                    - 🔍 Dynamic plateau detection using rolling standard deviation
                    - 📈 Interactive temperature curves with plateau markers
                    - 🎯 Shell detection and thermal journey visualization
                    - 📋 Detailed plateau metrics and production insights
                    - 📄 PDF export capabilities for reporting
                    """)
                else:
                    # Use position from sidebar
                    df = position_data[selected_position]['data']
                    
                    # Detect stable regions and transitions
                    # Use default values for flatness and duration (hidden from UI)
                    flat_th = 5  # Default flatness threshold
                    min_dur = 1  # Default minimum duration
                    
                    # Only show sensor selection for cleaner interface
                    sensor_options = []
                    sensor_mapping = {}  # Maps display names back to original column names

                    # Helper function to return original sensor names (no mapping)
                    def get_sensor_display_name(col_name):
                        """Return original sensor name from .dat file"""
                        # Keep original sensor names as specified by Antoine
                        return col_name

                    # Get all columns excluding Time and Head (case-insensitive)
                    head_cols = [col for col in df.columns if col.lower() == 'head']
                    exclude_cols = ['Time', 'Time_seconds', 'Unnamed: 6'] + head_cols

                    # Add all temperature sensor columns with appropriate display names
                    for col in df.columns:
                        if col not in exclude_cols:
                            display_name = get_sensor_display_name(col)
                            sensor_options.append(display_name)
                            sensor_mapping[display_name] = col

                    # Add average option if multiple sensors available
                    if len(sensor_options) > 1:
                        sensor_options.append('Average')
                        sensor_mapping['Average'] = 'Average'
                    
                    sensor_for_detection = st.selectbox(
                        get_text("sensor_label"), 
                        sensor_options, 
                        index=0,
                        help="Sélectionnez le capteur à utiliser pour la détection des plateaux"
                    )
                    
                    # Convert display name back to original column name for processing
                    actual_sensor = sensor_mapping.get(sensor_for_detection, sensor_for_detection)
                
                # State management: Clear results when settings change
                current_settings = {
                    'position': selected_position,
                    'flat_th': flat_th,
                    'min_dur': min_dur,
                    'sensor': actual_sensor
                }
                
                # Check if settings have changed
                if 'previous_settings' not in st.session_state:
                    st.session_state.previous_settings = current_settings
                elif st.session_state.previous_settings != current_settings:
                    # Settings changed - clear any cached results
                    st.session_state.pop("detected_shells", None)
                    st.session_state.previous_settings = current_settings
                    # Force rerun to clear stale UI elements
                    st.rerun()
                
                # Calculate data resolution
                df_res = 1.0 / (df['Time_seconds'].iloc[1] - df['Time_seconds'].iloc[0]) if len(df) > 1 else 1.0
                
                # Prepare sensor data
                if actual_sensor == 'Average':
                    # Calculate average of all temperature sensors
                    temp_cols = [col for col in df.columns if col not in ['Time', 'Time_seconds', 'Unnamed: 6']]
                    sensor_data = df[temp_cols].mean(axis=1)
                else:
                    sensor_data = df[actual_sensor]
                
                # Dynamic plateau detection with rolling standard deviation
                def detect_plateaus_rolling_std(data, sensor_data, flat_th, min_dur, df_res):
                    plateaus = []
                    
                    # Calculate rolling standard deviation with 0.5 second window
                    # Ensure minimum window size of 3 for meaningful std calculation
                    window_size = max(3, int(1/df_res * 0.5))
                    roll_std = pd.Series(sensor_data).rolling(window=window_size, center=True).std()
                    
                    # Fill NaN values at the beginning and end
                    roll_std = roll_std.bfill().ffill()
                    
                    # Identify stable regions
                    stable = roll_std < flat_th
                    
                    # Find continuous stable segments
                    stable_segments = []
                    current_segment = None
                    
                    for i in range(len(stable)):
                        if stable.iloc[i]:
                            if current_segment is None:
                                current_segment = {'start': i}
                            current_segment['end'] = i
                        else:
                            if current_segment is not None:
                                stable_segments.append(current_segment)
                                current_segment = None
                    
                    # Handle final segment
                    if current_segment is not None:
                        stable_segments.append(current_segment)
                    

                    
                    # Filter segments by minimum duration
                    for segment in stable_segments:
                        start_time = data['Time_seconds'].iloc[segment['start']]
                        end_time = data['Time_seconds'].iloc[segment['end']]
                        duration = end_time - start_time
                        
                        if duration >= min_dur:
                            # Extract temperatures for this plateau
                            plateau_temps = sensor_data.iloc[segment['start']:segment['end']+1]
                            avg_temp = plateau_temps.mean()
                            
                            # Apply minimum temperature filter (lowered threshold for better detection)
                            min_temp_threshold = 100.0  # Lowered from 300°C to 100°C
                            if avg_temp >= min_temp_threshold:
                                plateau = {
                                    'start': segment['start'],
                                    'end': segment['end'],
                                    'start_time': start_time,
                                    'end_time': end_time,
                                    'duration': duration,
                                    'start_temp': plateau_temps.iloc[0],
                                    'end_temp': plateau_temps.iloc[-1],
                                    'avg_temp': avg_temp,
                                    'temps': plateau_temps.tolist(),
                                    'std': plateau_temps.std()
                                }
                                plateaus.append(plateau)
                    
                    # Keep only final summary for terminal output
                    print(f"Total shells detected: {len(plateaus)}")
                    return plateaus, roll_std, stable
                
                plateaus, roll_std, stable_mask = detect_plateaus_rolling_std(df, sensor_data, flat_th, min_dur, df_res)
                
                # Clear any cached results when no plateaus are detected
                if not plateaus:
                    st.session_state.pop("detected_shells", None)
                
                # Detection info removed for cleaner interface
                
                if not plateaus:
                    st.warning(get_text("no_plateau_found"))
                
                # Create temperature curve plot with rolling std
                fig = go.Figure()
                
                # Plot all sensor curves (Head sensor and Unnamed: 6 excluded)
                # Handle case-insensitive Head column (HEAD vs Head)
                head_cols = [col for col in df.columns if col.lower() == 'head']
                exclude_cols = ['Time', 'Time_seconds', 'Unnamed: 6'] + head_cols
                sensor_columns = [col for col in df.columns if col not in exclude_cols]
                colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

                # Return original sensor names from .dat file (no mapping)
                def get_display_name(sensor_name):
                    """Return original sensor name from .dat file"""
                    # Keep original sensor names as specified by Antoine
                    return sensor_name

                for i, sensor in enumerate(sensor_columns):
                    # Get display name for legend
                    display_name = get_display_name(sensor)
                    
                    fig.add_trace(go.Scatter(
                        x=df['Time_seconds'],
                        y=df[sensor],
                        mode='lines',
                        name=display_name,
                        line=dict(color=colors[i % len(colors)], width=2),
                        yaxis='y'
                    ))
                
                # Add separate average lines for start and end temperatures
                if plateaus:
                    # Calculate average of start temperatures (green line)
                    start_temps = [plateau['start_temp'] for plateau in plateaus]
                    if start_temps:
                        avg_start_temp = np.mean(start_temps)
                        fig.add_trace(go.Scatter(
                            x=df['Time_seconds'],
                            y=[avg_start_temp] * len(df),
                            mode='lines',
                            name='Average Start Temp',
                            line=dict(color='gray', width=3),
                            yaxis='y'
                        ))
                    
                    # Calculate average of end temperatures (red line)
                    end_temps = [plateau['end_temp'] for plateau in plateaus]
                    if end_temps:
                        avg_end_temp = np.mean(end_temps)
                        fig.add_trace(go.Scatter(
                            x=df['Time_seconds'],
                            y=[avg_end_temp] * len(df),
                            mode='lines',
                            name='Average End Temp',
                            line=dict(color='red', width=3, dash='dash'),
                            yaxis='y'
                        ))
                else:
                    # Fallback to original method if no plateaus detected
                    temp_cols = [col for col in df.columns if col not in ['Time', 'Time_seconds', 'Head', 'Unnamed: 6']]
                    average_temp = df[temp_cols].mean(axis=1)
                    
                    fig.add_trace(go.Scatter(
                        x=df['Time_seconds'],
                        y=average_temp,
                        mode='lines',
                        name='Average',
                        line=dict(color='white', width=3, dash='dash'),
                        yaxis='y'
                    ))
                
                # Rolling standard deviation visualization removed
                
                # IMPROVED SHELL DETECTION ALGORITHM
                # Detects shells chronologically to avoid missing shells at beginning
                threshold_temp = 150.0  # Shell end threshold (temperature drop)
                start_threshold = 480.0  # Shell start threshold (dynamic, can be adjusted)
                broken_piece_threshold = 150.0  # Broken piece detection threshold
                broken_piece_duration = 10.0  # Minimum duration in seconds to count as broken
                MIN_SHELL_DURATION = 9.0  # Minimum duration to count as valid shell (filters noise)

                temp_data = sensor_data.values
                time_data = df['Time_seconds'].values

                # Storage for detected shells
                shells = []
                shell_start_x = []
                shell_start_y = []
                shell_end_x = []
                shell_end_y = []
                position_changes = []
                broken_pieces = []

                # State machine for shell detection
                in_shell = False
                current_shell_start_idx = -1
                current_shell_peak_idx = -1
                current_shell_peak_temp = 0

                # Broken piece detection state
                below_threshold_start_idx = -1
                below_threshold_start_time = -1

                # Adaptive threshold: use percentile-based approach if data is available
                if len(temp_data) > 100:
                    # Calculate dynamic start threshold based on actual data range
                    max_temp = np.max(temp_data)
                    min_temp = np.min(temp_data)
                    temp_range = max_temp - min_temp

                    # Use different strategies based on temperature range
                    if max_temp > 450:
                        # High-temp range (500-600°C) - use 75th percentile
                        high_temps = temp_data[temp_data > 300]
                        if len(high_temps) > 10:
                            start_threshold = np.percentile(high_temps, 75)
                        else:
                            start_threshold = max_temp * 0.85
                    elif max_temp > 250:
                        # Medium-temp range (250-450°C) - use 60-70th percentile
                        valid_temps = temp_data[temp_data > 150]
                        if len(valid_temps) > 10:
                            # Use 65th percentile for better detection
                            start_threshold = np.percentile(valid_temps, 65)
                        else:
                            start_threshold = max_temp * 0.75
                    else:
                        # Low-temp range (<250°C) - use 70% of max
                        start_threshold = max_temp * 0.70

                    # Ensure reasonable minimum threshold (200°C)
                    start_threshold = max(200.0, start_threshold)

                    # Debug output for threshold selection
                    print(f"Adaptive threshold: max={max_temp:.1f}°C, threshold={start_threshold:.1f}°C")

                # Scan chronologically through all temperature data
                for i in range(len(temp_data)):
                    current_temp = temp_data[i]
                    current_time = time_data[i]

                    # BROKEN PIECE DETECTION: Track periods below threshold
                    if current_temp <= broken_piece_threshold:
                        # Start tracking if not already tracking
                        if below_threshold_start_idx == -1:
                            below_threshold_start_idx = i
                            below_threshold_start_time = current_time
                    else:
                        # Temperature rose above threshold
                        if below_threshold_start_idx != -1:
                            # Calculate duration below threshold
                            duration_below = current_time - below_threshold_start_time

                            # If duration exceeds threshold, it's a broken piece
                            if duration_below > broken_piece_duration:
                                broken_piece = {
                                    'piece_number': len(broken_pieces) + 1,
                                    'start_idx': below_threshold_start_idx,
                                    'start_time': below_threshold_start_time,
                                    'end_idx': i - 1,
                                    'end_time': time_data[i - 1],
                                    'duration': duration_below,
                                    'avg_temp': np.mean(temp_data[below_threshold_start_idx:i])
                                }
                                broken_pieces.append(broken_piece)

                            # Reset tracking
                            below_threshold_start_idx = -1
                            below_threshold_start_time = -1

                    if not in_shell:
                        # SHELL START DETECTION: Look for temperature rising above threshold
                        if current_temp >= start_threshold:
                            in_shell = True
                            current_shell_start_idx = i
                            current_shell_peak_idx = i
                            current_shell_peak_temp = current_temp
                    else:
                        # INSIDE SHELL: Track peak temperature
                        if current_temp > current_shell_peak_temp:
                            current_shell_peak_idx = i
                            current_shell_peak_temp = current_temp

                        # SHELL END DETECTION: Look for temperature dropping below threshold
                        if current_temp <= threshold_temp:
                            # Find the last peak before this drop
                            # Search backwards from current position to find last local maximum
                            end_peak_idx = current_shell_peak_idx
                            end_peak_temp = current_shell_peak_temp

                            # Look for a better end peak just before the drop
                            for j in range(i - 1, max(current_shell_start_idx, i - 50), -1):
                                if j <= 0 or j >= len(temp_data) - 1:
                                    continue

                                check_temp = temp_data[j]
                                prev_temp = temp_data[j - 1]
                                next_temp = temp_data[j + 1]

                                # Local maximum with minimum temperature requirement
                                if check_temp > prev_temp and check_temp > next_temp and check_temp >= 200:
                                    end_peak_idx = j
                                    end_peak_temp = check_temp
                                    break

                            # Calculate shell duration
                            shell_duration = time_data[end_peak_idx] - time_data[current_shell_start_idx]

                            # Only record shell if it meets minimum duration (filters noise)
                            if shell_duration >= MIN_SHELL_DURATION:
                                # Record the shell
                                shell = {
                                    'shell_number': len(shells) + 1,
                                    'start_idx': current_shell_start_idx,
                                    'start_time': time_data[current_shell_start_idx],
                                    'start_temp': current_shell_peak_temp,
                                    'end_idx': end_peak_idx,
                                    'end_time': time_data[end_peak_idx],
                                    'end_temp': end_peak_temp,
                                    'peak_idx': current_shell_peak_idx,
                                    'peak_temp': current_shell_peak_temp,
                                    'duration': shell_duration
                                }
                                shells.append(shell)

                                # Add to visualization arrays
                                shell_start_x.append(time_data[current_shell_peak_idx])
                                shell_start_y.append(current_shell_peak_temp)
                                shell_end_x.append(time_data[end_peak_idx])
                                shell_end_y.append(end_peak_temp)

                                # Record position change
                                position_change = {
                                    'event_number': len(position_changes) + 1,
                                    'timestamp': time_data[i],
                                    'temperature': current_temp,
                                    'sensor': actual_sensor
                                }
                                position_changes.append(position_change)

                            # Reset state for next shell
                            in_shell = False
                            current_shell_start_idx = -1
                            current_shell_peak_idx = -1
                            current_shell_peak_temp = 0

                # Handle case where recording ends while still in a shell
                if in_shell and current_shell_peak_idx != -1:
                    end_idx = len(temp_data) - 1

                    # Find last significant peak before end
                    end_peak_idx = current_shell_peak_idx
                    end_peak_temp = current_shell_peak_temp

                    for j in range(end_idx - 1, max(current_shell_start_idx, end_idx - 50), -1):
                        if j <= 0 or j >= len(temp_data) - 1:
                            continue
                        check_temp = temp_data[j]
                        prev_temp = temp_data[j - 1]
                        next_temp = temp_data[j + 1]

                        if check_temp > prev_temp and check_temp > next_temp and check_temp >= 200:
                            end_peak_idx = j
                            end_peak_temp = check_temp
                            break

                    # Calculate shell duration
                    shell_duration = time_data[end_peak_idx] - time_data[current_shell_start_idx]

                    # Only record shell if it meets minimum duration (filters noise)
                    if shell_duration >= MIN_SHELL_DURATION:
                        shell = {
                            'shell_number': len(shells) + 1,
                            'start_idx': current_shell_start_idx,
                            'start_time': time_data[current_shell_start_idx],
                            'start_temp': current_shell_peak_temp,
                            'end_idx': end_peak_idx,
                            'end_time': time_data[end_peak_idx],
                            'end_temp': end_peak_temp,
                            'peak_idx': current_shell_peak_idx,
                            'peak_temp': current_shell_peak_temp,
                            'duration': shell_duration
                        }
                        shells.append(shell)
                        shell_start_x.append(time_data[current_shell_peak_idx])
                        shell_start_y.append(current_shell_peak_temp)
                        shell_end_x.append(time_data[end_peak_idx])
                        shell_end_y.append(end_peak_temp)

                # Handle case where recording ends while still below threshold (broken piece)
                if below_threshold_start_idx != -1:
                    end_idx = len(temp_data) - 1
                    duration_below = time_data[end_idx] - below_threshold_start_time

                    if duration_below > broken_piece_duration:
                        broken_piece = {
                            'piece_number': len(broken_pieces) + 1,
                            'start_idx': below_threshold_start_idx,
                            'start_time': below_threshold_start_time,
                            'end_idx': end_idx,
                            'end_time': time_data[end_idx],
                            'duration': duration_below,
                            'avg_temp': np.mean(temp_data[below_threshold_start_idx:end_idx+1])
                        }
                        broken_pieces.append(broken_piece)

                # Store counts for summary
                total_shells_detected = len(shells)
                total_broken_pieces = len(broken_pieces)
                total_pieces = total_shells_detected + total_broken_pieces
                shattering_rate = (total_broken_pieces / total_pieces * 100) if total_pieces > 0 else 0

                # PLATEAU DETECTION FOR EACH SHELL
                # Analyze temperature stability within each shell (1-2 second plateaus)
                # HEAD SENSOR SPECIAL LOGIC: Inverted profile - find LOWEST point
                is_head_sensor = actual_sensor.lower() == 'head'

                def detect_shell_plateau(shell_data, temp_data, time_data, is_head=False, min_duration=1.0, max_duration=2.5, stability_threshold=5.0):
                    """
                    Detect temperature plateau within a shell
                    For Head sensor: inverted logic - finds LOWEST stable point (>130-140°C)
                    For other sensors: finds HIGHEST stable point
                    Returns: plateau info dict or None
                    """
                    start_idx = shell_data['start_idx']
                    end_idx = shell_data['end_idx']

                    if end_idx - start_idx < 5:  # Too short to have plateau
                        return None

                    # Extract shell temperature segment
                    shell_temps = temp_data[start_idx:end_idx+1]
                    shell_times = time_data[start_idx:end_idx+1]

                    if len(shell_temps) < 5:
                        return None

                    # HEAD SENSOR: Use lower threshold (130-140°C) for valid temps
                    head_min_temp = 130.0 if is_head else 0
                    head_max_temp = 500.0  # Upper limit to filter out noise

                    # Filter temperatures for Head sensor
                    if is_head:
                        valid_temps_mask = (shell_temps >= head_min_temp) & (shell_temps <= head_max_temp)
                        if not np.any(valid_temps_mask):
                            return None

                    # Look for stable regions using rolling standard deviation
                    window_size = max(3, int(len(shell_temps) * 0.2))  # 20% window

                    best_plateau = None
                    min_std = float('inf')

                    # Scan for most stable region
                    for i in range(len(shell_temps) - window_size):
                        window_temps = shell_temps[i:i+window_size]
                        window_std = np.std(window_temps)
                        window_duration = shell_times[i+window_size-1] - shell_times[i]

                        # For Head sensor, check if temps are in valid range
                        if is_head:
                            window_mean = np.mean(window_temps)
                            if window_mean < head_min_temp or window_mean > head_max_temp:
                                continue

                        # Check if this window is stable enough and within duration range
                        if window_std < stability_threshold and min_duration <= window_duration <= max_duration:
                            if window_std < min_std:
                                min_std = window_std
                                best_plateau = {
                                    'start_idx': start_idx + i,
                                    'end_idx': start_idx + i + window_size - 1,
                                    'start_time': shell_times[i],
                                    'end_time': shell_times[i+window_size-1],
                                    'duration': window_duration,
                                    'avg_temp': np.mean(window_temps),
                                    'std': window_std,
                                    'is_stable': window_std < 3.0  # Very stable if std < 3°C
                                }

                    # If no stable plateau found, use temperature extreme
                    if best_plateau is None:
                        if is_head:
                            # HEAD SENSOR: Find LOWEST temperature above threshold
                            valid_temps = shell_temps[(shell_temps >= head_min_temp) & (shell_temps <= head_max_temp)]
                            if len(valid_temps) > 0:
                                min_temp = np.min(valid_temps)
                                min_idx = np.where(shell_temps == min_temp)[0][0]
                            else:
                                min_idx = np.argmin(shell_temps)

                            best_plateau = {
                                'start_idx': start_idx + min_idx,
                                'end_idx': start_idx + min_idx,
                                'start_time': shell_times[min_idx],
                                'end_time': shell_times[min_idx],
                                'duration': 0,
                                'avg_temp': shell_temps[min_idx],
                                'std': 0,
                                'is_stable': False
                            }
                        else:
                            # NORMAL SENSORS: Find HIGHEST temperature (peak)
                            peak_idx = np.argmax(shell_temps)
                            best_plateau = {
                                'start_idx': start_idx + peak_idx,
                                'end_idx': start_idx + peak_idx,
                                'start_time': shell_times[peak_idx],
                                'end_time': shell_times[peak_idx],
                                'duration': 0,
                                'avg_temp': shell_temps[peak_idx],
                                'std': 0,
                                'is_stable': False
                            }

                    return best_plateau

                # Add plateau analysis to each shell
                for shell in shells:
                    plateau = detect_shell_plateau(shell, temp_data, time_data, is_head=is_head_sensor)
                    shell['plateau'] = plateau

                    # Add representative temperature (average for stable, peak for unstable)
                    if plateau:
                        shell['representative_temp'] = plateau['avg_temp']
                        if is_head_sensor:
                            shell['temp_stability'] = 'Head (Low)' if plateau['is_stable'] else 'Head (Unstable)'
                        else:
                            shell['temp_stability'] = 'Stable' if plateau['is_stable'] else 'Unstable'
                    else:
                        shell['representative_temp'] = shell['peak_temp']
                        shell['temp_stability'] = 'No Plateau'

                # Add shell start markers
                if shell_start_x and shell_start_y:
                    fig.add_trace(go.Scatter(
                        x=shell_start_x,
                        y=shell_start_y,
                        mode='markers',
                        name=f"Shell Start (n={total_shells_detected})",
                        marker=dict(
                            color='green',
                            size=12,
                            symbol='triangle-up',
                            line=dict(color='darkgreen', width=2)
                        ),
                        hovertemplate="Shell Start<br>Time: %{x:.1f}s<br>Start Temp: %{y:.1f}°C<extra></extra>",
                        showlegend=True
                    ))

                # Add shell end markers
                if shell_end_x and shell_end_y:
                    fig.add_trace(go.Scatter(
                        x=shell_end_x,
                        y=shell_end_y,
                        mode='markers',
                        name="Shell End",
                        marker=dict(
                            color='red',
                            size=12,
                            symbol='triangle-down',
                            line=dict(color='darkred', width=2)
                        ),
                        hovertemplate="Shell End<br>Time: %{x:.1f}s<br>End Temp: %{y:.1f}°C<extra></extra>",
                        showlegend=True
                    ))

                # Add plateau markers (representative temperatures)
                plateau_x = []
                plateau_y = []
                plateau_text = []
                for shell in shells:
                    if shell.get('plateau') and shell['plateau']['is_stable']:
                        plateau = shell['plateau']
                        # Mark the midpoint of the plateau
                        mid_time = (plateau['start_time'] + plateau['end_time']) / 2
                        plateau_x.append(mid_time)
                        plateau_y.append(plateau['avg_temp'])
                        if is_head_sensor:
                            plateau_text.append(f"Shell {shell['shell_number']}: {plateau['avg_temp']:.1f}°C (Head-Low)")
                        else:
                            plateau_text.append(f"Shell {shell['shell_number']}: {plateau['avg_temp']:.1f}°C (Stable)")

                if plateau_x and plateau_y:
                    marker_color = 'cyan' if is_head_sensor else 'yellow'
                    marker_symbol = 'triangle-down' if is_head_sensor else 'diamond'
                    marker_name = "Head Plateaus (Low)" if is_head_sensor else "Stable Plateaus"

                    fig.add_trace(go.Scatter(
                        x=plateau_x,
                        y=plateau_y,
                        mode='markers',
                        name=marker_name,
                        marker=dict(
                            color=marker_color,
                            size=10,
                            symbol=marker_symbol,
                            line=dict(color='blue' if is_head_sensor else 'orange', width=2)
                        ),
                        text=plateau_text,
                        hovertemplate="%{text}<extra></extra>",
                        showlegend=True
                    ))

                # Add threshold line for reference
                fig.add_hline(y=threshold_temp, line_dash="solid", line_color="red",
                             annotation_text=f"Position Change Threshold ({threshold_temp}°C)",
                             annotation_position="bottom right")
                
                # Update layout
                fig.update_layout(
                    title=f"Temperature Curves - {selected_position}",
                    xaxis_title=get_text("time_seconds"),
                    yaxis_title=get_text("temperature_celsius"),
                    hovermode='x unified',
                    height=600
                )
                
                st.plotly_chart(fig, use_container_width=True)

                # Display shell detection summary
                if shells or broken_pieces:
                    st.subheader(f"📊 Shell Detection Summary - {selected_position}")

                    # Calculate measurement time
                    total_measurement_time = time_data[-1] - time_data[0] if len(time_data) > 0 else 0

                    # Create summary metrics - Row 1
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Total Shells Detected", total_shells_detected)
                    with col2:
                        st.metric("Measurement Time", f"{total_measurement_time:.1f}s")
                    with col3:
                        if shells:
                            # Calculate duration including gap to next piece (Antoine's specification)
                            # Duration = stationary time + time until next piece starts
                            durations_with_gaps = []
                            for i in range(len(shells)):
                                if i < len(shells) - 1:
                                    # Time from this shell start to next shell start
                                    duration_with_gap = shells[i+1]['start_time'] - shells[i]['start_time']
                                    durations_with_gaps.append(duration_with_gap)
                                else:
                                    # Last shell: use only stationary duration
                                    durations_with_gaps.append(shells[i]['duration'])
                            avg_shell_duration = np.mean(durations_with_gaps)
                            st.metric("Avg Shell Duration", f"{avg_shell_duration:.1f}s")
                        else:
                            st.metric("Avg Shell Duration", "N/A")
                    with col4:
                        production_rate = (total_shells_detected / total_measurement_time * 60) if total_measurement_time > 0 else 0
                        st.metric("Production Rate", f"{production_rate:.1f} pcs/min")

                    # Create summary metrics - Row 2 (Broken Pieces & Quality)
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Broken Pieces", total_broken_pieces,
                                  delta=None if total_broken_pieces == 0 else f"❌ {total_broken_pieces} broken",
                                  delta_color="inverse")
                    with col2:
                        st.metric("Total Pieces", total_pieces)
                    with col3:
                        # Shattering rate with color coding
                        shattering_color = "🟢" if shattering_rate < 5 else ("🟡" if shattering_rate < 15 else "🔴")
                        st.metric("Shattering Rate", f"{shattering_color} {shattering_rate:.1f}%")
                    with col4:
                        quality_score = 100 - shattering_rate
                        st.metric("Quality Score", f"{quality_score:.1f}%")

                    # Temperature summary from detected shells
                    if shells:
                        avg_start_temp = np.mean([s['start_temp'] for s in shells])
                        avg_end_temp = np.mean([s['end_temp'] for s in shells])
                        avg_peak_temp = np.mean([s['peak_temp'] for s in shells])

                        st.subheader("🌡️ Temperature Summary")
                        temp_summary = {
                            'Metric': ['Average Start Temp', 'Average Peak Temp', 'Average End Temp', 'Avg Delta (Start-End)'],
                            'Value (°C)': [
                                f"{avg_start_temp:.1f}",
                                f"{avg_peak_temp:.1f}",
                                f"{avg_end_temp:.1f}",
                                f"{avg_start_temp - avg_end_temp:.1f}"
                            ]
                        }
                        temp_summary_df = pd.DataFrame(temp_summary)
                        st.dataframe(temp_summary_df, use_container_width=True, hide_index=True)

                        # Plateau Analysis Table
                        st.subheader("📊 Plateau Analysis (1-2s Stability)")

                        if is_head_sensor:
                            st.info("🔄 **Head Sensor Mode Active**: Using inverted logic - finding LOWEST stable temperatures above 130°C threshold.")
                            st.markdown("""
                            **Representative temperatures** for each shell (Head Sensor):
                            - **Head (Low)**: Average of LOWEST stable temperatures in 1-2s plateau (>130°C)
                            - **Head (Unstable)**: Minimum temperature (no stable plateau found)
                            """)
                        else:
                            st.markdown("""
                            **Representative temperatures** for each shell:
                            - **Stable**: Average temperature of 1-2 second plateau (low variation)
                            - **Unstable**: Peak temperature (high variation, no stable plateau)
                            """)

                        plateau_data = []
                        stable_count = 0
                        for shell in shells:
                            plateau = shell.get('plateau')
                            if plateau:
                                stability = "✅ Stable" if plateau['is_stable'] else "⚠️ Unstable"
                                if plateau['is_stable']:
                                    stable_count += 1

                                plateau_data.append({
                                    'Shell #': shell['shell_number'],
                                    'Representative Temp (°C)': f"{shell['representative_temp']:.1f}",
                                    'Plateau Duration (s)': f"{plateau['duration']:.2f}" if plateau['duration'] > 0 else "N/A",
                                    'Temp Std Dev (°C)': f"{plateau['std']:.2f}",
                                    'Stability': stability
                                })

                        if plateau_data:
                            plateau_df = pd.DataFrame(plateau_data)
                            st.dataframe(plateau_df, use_container_width=True, hide_index=True)

                            # Stability statistics
                            stability_rate = (stable_count / len(shells) * 100) if shells else 0
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Stable Plateaus", f"{stable_count}/{len(shells)}")
                            with col2:
                                st.metric("Stability Rate", f"{stability_rate:.1f}%")
                            with col3:
                                avg_representative_temp = np.mean([s['representative_temp'] for s in shells])
                                st.metric("Avg Representative Temp", f"{avg_representative_temp:.1f}°C")

                    # Display broken pieces details if any detected
                    if broken_pieces:
                        st.subheader("💔 Broken Pieces Details")
                        st.markdown(f"""
                        **Detected {total_broken_pieces} broken piece(s)** - pieces that stayed below {broken_piece_threshold}°C
                        for more than {broken_piece_duration} seconds (likely exploded during tempering).
                        """)

                        broken_pieces_data = []
                        for bp in broken_pieces:
                            broken_pieces_data.append({
                                'Piece #': bp['piece_number'],
                                'Start Time (s)': f"{bp['start_time']:.1f}",
                                'End Time (s)': f"{bp['end_time']:.1f}",
                                'Duration (s)': f"{bp['duration']:.1f}",
                                'Avg Temp (°C)': f"{bp['avg_temp']:.1f}"
                            })

                        broken_df = pd.DataFrame(broken_pieces_data)
                        st.dataframe(broken_df, use_container_width=True, hide_index=True)

                # Display detected plateaus with comprehensive metrics
                # Only show results if plateaus are actually detected in current run
                if plateaus and len(plateaus) > 0:
                    st.subheader(f"📊 Résumé des Températures - Position: {selected_position}")
                    
                    # Calculate overall averages for start and end temperatures
                    all_start_temps = []
                    all_end_temps = []
                    
                    for plateau in plateaus:
                        start_idx = plateau['start']
                        end_idx = plateau['end']
                        
                        # Extract start and end temperatures from the sensor used for detection
                        start_temp = sensor_data.iloc[start_idx]
                        end_temp = sensor_data.iloc[end_idx]
                        
                        all_start_temps.append(start_temp)
                        all_end_temps.append(end_temp)
                    
                    # Calculate averages
                    avg_start_temp = np.mean(all_start_temps) if all_start_temps else 0
                    avg_end_temp = np.mean(all_end_temps) if all_end_temps else 0
                    avg_delta_t = avg_start_temp - avg_end_temp
                    
                    # Create summary table
                    summary_data = {
                        'Metric': ['Average Start Temperature', 'Average End Temperature', 'Average Delta-T'],
                        'Value': [f"{avg_start_temp:.1f}°C", f"{avg_end_temp:.1f}°C", f"{avg_delta_t:.1f}°C"]
                    }
                    
                    summary_df = pd.DataFrame(summary_data)
                    
                    # Analysis complete - clean interface without shell summary
                
                # Temperature comparison table - concise format
                if all_start_temps and all_end_temps:
                    st.subheader("🌡️ Temperature Summary")
                    
                    # Create concise temperature comparison
                    temp_comparison_data = {
                        'Metric': ['Start Avg', 'End Avg', 'Delta'],
                        'Temperature (°C)': [
                            f"{np.mean(all_start_temps):.1f}",
                            f"{np.mean(all_end_temps):.1f}",
                            f"{np.mean(all_start_temps) - np.mean(all_end_temps):.1f}"
                        ]
                    }
                    
                    temp_comparison_df = pd.DataFrame(temp_comparison_data)
                    st.dataframe(temp_comparison_df, use_container_width=True, hide_index=True)
                
                # Shell start events table removed - using position change detection instead
                
                # # PDF Export Section (Always Available)
                # st.subheader(get_text("pdf_export"))
                # 
                # # PDF Configuration
                # col1, col2 = st.columns(2)
                # with col1:
                #     report_title = st.text_input("Report Title", value=f"Thermal Analysis - {selected_position}")
                #     analyst_name = st.text_input("Analyst Name", value="Sediver Analyst")
                # 
                # with col2:
                #     add_watermark = st.checkbox("Add 'Internal Use Only' watermark", value=False)
                # 
                # # Section toggles
                # st.write("**Include Sections:**")
                # col1, col2, col3 = st.columns(3)
                # with col1:
                #     include_executive = st.checkbox("Executive Summary", value=True)
                #     include_shell_table = st.checkbox("Shell Detection Table", value=True)
                # with col2:
                #     include_charts = st.checkbox("Temperature Charts", value=True)
                #     include_alerts = st.checkbox("Quality Alerts", value=True)
                # with col3:
                #     include_recommendations = st.checkbox("Recommendations", value=True)
                # 
                # # Generate PDF button
                # if st.button("📄 Generate PDF Report", type="primary"):
                #     with st.spinner("🔄 Generating PDF report..."):
                #         try:
                #             # Prepare section configuration (Full PDF by default)
                #             include_sections = {
                #                 'executive_summary': include_executive,
                #                 'shell_detection': include_shell_table,
                #                 'temperature_charts': include_charts,
                #                 'quality_alerts': include_alerts,
                #                 'recommendations': include_recommendations
                #             }
                #             
                #             # Convert plateaus to the format expected by PDF generator
                #             pdf_plateaus = []
                #             if plateaus:  # Only process if plateaus exist
                #                 for plateau in plateaus:
                #                     start_time = df['Time_seconds'].iloc[plateau['start']]
                #                     end_time = df['Time_seconds'].iloc[plateau['end']]
                #                     pdf_plateaus.append({
                #                         'start_time': start_time,
                #                         'end_time': end_time,
                #                         'duration': plateau['duration']
                #                     })
                #             
                #             # Generate PDF (works even with no plateaus)
                #             pdf_bytes = generate_pdf_report(
                #                 plateaus=pdf_plateaus,
                #                 df=df,
                #                 fig=fig,
                #                 report_title=report_title,
                #                 analyst_name=analyst_name,
                #                 include_sections=include_sections,
                #                 pdf_type="full pdf",
                #                 add_watermark=add_watermark
                #             )
                #             
                #             # Get current date for filename
                #             today = datetime.now().strftime("%Y-%m-%d")
                #             filename = f"{report_title.replace(' ', '_')}_{today}.pdf"
                #             
                #             # Download button
                #             st.download_button(
                #                 label="📥 Download PDF Report",
                #                 data=pdf_bytes,
                #                 file_name=filename,
                #                 mime="application/pdf",
                #                 help="Download the generated PDF report"
                #             )
                #             
                #             st.success(f"✅ PDF report generated successfully! ({len(pdf_bytes)} bytes)")
                #             
                #         except Exception as e:
                #             st.error(f"❌ PDF generation failed: {str(e)}")
                #             st.write("**Debug info:**")
                #             st.write(f"- Plateaus count: {len(plateaus) if plateaus else 0}")
                #             st.write(f"- DataFrame shape: {df.shape}")
                #             st.write(f"- Figure type: {type(fig)}")
            
        # Individual Glass Shell Analysis feature removed for cleaner interface
            
        # Old Peak Temperature Data section removed - replaced by new plateau detection logic
            
        if True:
            with st.expander(get_text("multi_position_header"), expanded=False):
                
                if not selected_position:
                    st.info(get_text("upload_data_first_multi"))
                    st.markdown("""
                    **This analysis will provide:**
                    - 🏭 Multi-position glass shell journey visualization
                    - 📊 Primary sensor temperature comparison across positions
                    - 📈 Composite thermal journey plot
                    - 📋 Position-by-position comparison table
                    - 🔍 Cross-position temperature analysis
                    - ⏱️ Duration and sample count metrics
                    """)
                else:
                    if len(position_data) > 1:
                        st.info("📍 Reconstructing glass shell journey across toughening line")
                        
                        # Create composite plot
                        fig = go.Figure()
                        
                        colors = px.colors.qualitative.Set3

                        # Flexible sensor mapping for display names (handles both formats)
                        def get_display_name(sensor_name):
                            """Return original sensor name from .dat file"""
                            # Keep original sensor names as specified by Antoine
                            return sensor_name

                        for i, (pos_name, pos_info) in enumerate(position_data.items()):
                            df = pos_info['data']
                            
                            # Use first available sensor (excluding Head and Unnamed: 6) for composite view
                            # Handle case-insensitive Head column
                            head_cols = [col for col in df.columns if col.lower() == 'head']
                            exclude_cols = ['Time', 'Time_seconds', 'Unnamed: 6'] + head_cols
                            available_sensors = [col for col in df.columns if col not in exclude_cols]
                            if available_sensors:
                                sensor_to_use = available_sensors[0]
                                # Get display name for sensor
                                display_name = get_display_name(sensor_to_use)
                                
                                fig.add_trace(go.Scatter(
                                    x=df['Time_seconds'],
                                    y=df[sensor_to_use],
                                    mode='lines',
                                    name=f"{pos_name} ({display_name})",
                                    line=dict(color=colors[i % len(colors)], width=2)
                                ))
                        
                        fig.update_layout(
                            title=get_text("multi_position_journey_title"),
                            xaxis_title=get_text("time_seconds"),
                            yaxis_title=get_text("temperature_celsius"),
                            hovermode='x unified',
                            height=600
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Position comparison table
                        st.subheader(get_text("position_comparison"))
                        
                        comparison_data = []
                        for pos_name, pos_info in position_data.items():
                            df = pos_info['data']
                            available_sensors = [col for col in df.columns if col not in ['Time', 'Time_seconds', 'Head', 'Unnamed: 6']]
                            if available_sensors:
                                sensor_to_use = available_sensors[0]
                                comparison_data.append({
                                    'Position': pos_name,
                                    get_text('temp_max'): df[sensor_to_use].max(),
                                    get_text('temp_min'): df[sensor_to_use].min(),
                                    get_text('temp_avg'): df[sensor_to_use].mean(),
                                    get_text('duration'): df['Time_seconds'].max(),
                                    get_text('samples'): len(df)
                                })
                        
                        if comparison_data:
                            comparison_df = pd.DataFrame(comparison_data)
                            st.dataframe(comparison_df, use_container_width=True)
                    
                    else:
                        st.warning(get_text("upload_multiple_files"))

            
        # Interactive Plotly View feature removed for cleaner interface

            
        # Full Line Thermal Journey feature removed for cleaner interface

            
        if True:
            with st.expander(get_text("ai_summary_header"), expanded=False):
                
                # New single-section layout
                st.header("Generate Insight Briefing")
                
                # Global Identification Section
                st.subheader("Global Identification")
                plant = st.text_input("Plant")
                line_number = st.text_input("Line #")
                glass_shell = st.text_input("Glass shell")
                campaign_number = st.text_input("Campaign #")
                # Use smart calendar input with extracted file date
                default_date = st.session_state.get('file_date', date.today())
                time_date = st.date_input("Time & date", value=default_date)
                
                # Toughening Parameters Section
                st.subheader("Toughening Parameters")
                line_speed = st.text_input("Line speed (pcs/min)")
                temperature_u4 = st.text_input("Temperature U4 furnace (°C)")
                toughening_positions = st.text_input("Number of toughening positions with air / open positions")
                # Split pressure into two fields as requested by Antoine
                col_p1, col_p2 = st.columns(2)
                with col_p1:
                    air_pressure_top = st.text_input("GS Top (bar)")
                with col_p2:
                    air_pressure_bottom = st.text_input("GS Bottom (bar)")
                air_temperature = st.text_input("Air temperature (°C)")
                rotation_speed = st.text_input("Rotation speed (% / rpm)")
                
                # Generate Insight Briefing Button
                if st.button("Generate Insight Briefing", type="primary"):
                    if position_data:
                        try:
                            print("[DEBUG] Generate Insight Briefing button clicked")
                            print(f"[DEBUG] Position data available: {list(position_data.keys())}")
                            
                            # Collect UI metadata
                            print("[DEBUG] Step 1: Collecting UI metadata")
                            metadata = collect_ui_metadata(
                                plant, line_number, glass_shell, campaign_number, time_date,
                                line_speed, temperature_u4, toughening_positions, air_pressure_top, air_pressure_bottom, air_temperature, rotation_speed
                            )
                            print(f"[DEBUG] Step 1 completed: {metadata}")
                            
                            # Generate PDF with basic metadata only
                            print("[DEBUG] Step 2: Generating PDF")
                            pdf_buffer = generate_insight_briefing_pdf(metadata, [], [], position_data)
                            print("[DEBUG] Step 2 completed: PDF generated successfully")
                            
                            # Create download button
                            st.success("✅ Insight Briefing PDF generated successfully!")
                            
                            # Display confirmation
                            st.subheader("📋 Briefing Generated")
                            
                            # Download button
                            st.download_button(
                                label="📥 Download Insight Briefing PDF",
                                data=pdf_buffer.getvalue(),
                                file_name=f"SEDIVER_Insight_Briefing_{metadata.get('date', 'report')}.pdf",
                                mime="application/pdf",
                                type="primary"
                            )
                            
                        except Exception as e:
                            st.error(f"Error generating PDF: {str(e)}")
                            st.write("Please ensure data files are properly loaded and try again.")
                    else:
                        st.warning("⚠️ Please upload thermal data files first to generate the Insight Briefing.")



else:
    st.info(get_text("upload_prompt"))
    
    # Sample data info
    st.subheader(get_text("expected_format"))
    st.code("""
[Connect DataFile][1.1]
Date:;04/06/2025
Time:;14:48:53,583
Unit:;°C
Resolution:;0,05
Values:;5
Time;Head;1;2;3;4;
00:00:00,000;440,1;445,5;470,1;472,5;489,9;
00:00:00,050;456,5;463,7;465,8;475,3;478,6;
...
    """)
    
    # Analysis capabilities removed for cleaner interface

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>SEDIVER | Glass Toughening Analysis v1.0</p>
    </div>
    """,
    unsafe_allow_html=True
)

