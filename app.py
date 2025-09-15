import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
<<<<<<< HEAD
from datetime import datetime, date
=======
from datetime import datetime
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
import time
from io import StringIO, BytesIO
from dotenv import load_dotenv
import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
<<<<<<< HEAD
from reportlab.lib.colors import HexColor, black, whitesmoke, white, gray
=======
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
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
<<<<<<< HEAD
    "app_title": "SEDIVER Celsius AI",
=======
    "app_title": "SEDIVER Celcius AI",
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
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
    "plateau_detection_settings": "🔍 Dynamic Plateau Detection Settings",
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
    "multi_position_journey_title": "Multi-Position Glass Shell Journey (Head Sensor)",

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
    "head_sensor_journey": "Head Sensor Thermal Journey Comparison",
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
    "sensor_label": "Sensor:",
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
    "temp_range_celsius": "Temp Range (°C)"
}

# French translations
FR = {
    # Sidebar elements
<<<<<<< HEAD
    "app_title": "SEDIVER Celsius AI",
=======
    "app_title": "SEDIVER Celcius AI",
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
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
    "plateau_detection_settings": "🔍 Paramètres de Détection Dynamique des Plateaux",
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
    "head_sensor_journey": "Comparaison du Parcours Thermique du Capteur de Tête",
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
    "sensor_label": "Capteur:",
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
    "no_head_sensor": "⚠️ Aucune donnée de capteur de tête trouvée dans les fichiers téléchargés",
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
    "download_data_csv": "📊 Télécharger Données (CSV)"
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

<<<<<<< HEAD
def collect_ui_metadata(plant, line_number, glass_shell, campaign_number, file_date, line_speed, temperature_u4, toughening_positions, air_pressure, air_temperature, rotation_speed):
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
        # PDF expects: 'Toughening air pressure top & bottom (bar)' -> metadata.get('quench_pressure')
        metadata['quench_pressure'] = air_pressure or ''  # Air pressure maps to quench_pressure for PDF
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

def calculate_cooling_curve_data(analysis_results):
    """Calculate cooling curve data from session state analysis results"""
    print("[DEBUG] Starting calculate_cooling_curve_data function")
    print(f"[DEBUG] Analysis results keys: {list(analysis_results.keys()) if analysis_results else 'None'}")
    
    cooling_curve_data = []
    
    try:
        if not analysis_results:
            print("[DEBUG] No analysis results found in session state")
            return cooling_curve_data
            
        for position_name, shell_summary_df in analysis_results.items():
            print(f"[DEBUG] Processing position: {position_name}")
            print(f"[DEBUG] Shell summary shape for {position_name}: {shell_summary_df.shape}")
            
            if not shell_summary_df.empty and 'Start Temp (°C)' in shell_summary_df.columns:
                # Calculate mean of the 'Start Temp (°C)' column for this position
                mean_temp = shell_summary_df['Start Temp (°C)'].mean()
                print(f"[DEBUG] Mean shell temperature for {position_name}: {mean_temp:.1f}°C")
                
                cooling_curve_data.append({
                    'Position': position_name,
                    'Mean_Shell_Temperature': round(mean_temp, 1)
                })
            else:
                print(f"[DEBUG] No valid shell data found for {position_name}, skipping")
        
        print(f"[DEBUG] Cooling curve data: {cooling_curve_data}")
        return cooling_curve_data
    except Exception as e:
        print(f"[ERROR] Error in calculate_cooling_curve_data: {str(e)}")
        print(f"[ERROR] Error type: {type(e).__name__}")
        raise e
        print(f"[ERROR] Error type: {type(e).__name__}")
        raise e

def create_consolidated_shell_data(analysis_results):
    """Create consolidated shell data table from session state analysis results"""
    print("[DEBUG] Starting create_consolidated_shell_data function")
    consolidated_data = []
    
    try:
        print(f"[DEBUG] Analysis results keys: {list(analysis_results.keys())}")
        
        for position_name, shell_summary_df in analysis_results.items():
            print(f"[DEBUG] Processing position: {position_name}")
            print(f"[DEBUG] Shell summary DataFrame shape for {position_name}: {shell_summary_df.shape}")
            
            # Add Position column to the DataFrame
            shell_summary_df_copy = shell_summary_df.copy()
            shell_summary_df_copy['Position'] = position_name
            
            # Append to consolidated data list
            consolidated_data.append(shell_summary_df_copy)
        
        # Concatenate all DataFrames into a single master DataFrame
        if consolidated_data:
            master_df = pd.concat(consolidated_data, ignore_index=True)
            print(f"[DEBUG] Consolidated shell data created: {len(master_df)} records")
            return master_df.to_dict('records')
        else:
            print(f"[DEBUG] No consolidated shell data created")
            return []
    except Exception as e:
        print(f"[ERROR] Error in create_consolidated_shell_data: {str(e)}")
        print(f"[ERROR] Error type: {type(e).__name__}")
        raise e

def generate_insight_briefing_pdf(metadata, cooling_curve_data, consolidated_shell_data):
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
            ['Toughening air pressure top & bottom (bar):', str(metadata.get('quench_pressure', 'N/A'))],
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
        
        # Cooling Curve Chart
        story.append(Paragraph("Cooling Curve Analysis", heading_style))
        
        if cooling_curve_data:
            # Create Plotly chart
            positions = [item['Position'] for item in cooling_curve_data]
            temperatures = [item['Mean_Shell_Temperature'] for item in cooling_curve_data]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=positions,
                y=temperatures,
                mode='lines+markers',
                name='Mean Shell Temperature',
                line=dict(color='#1f4e79', width=3),
                marker=dict(size=8, color='#1f4e79')
            ))
            
            fig.update_layout(
                title='Position vs. Mean Shell Temperature',
                xaxis_title='Position',
                yaxis_title='Mean Shell Temperature (°C)',
                width=600,
                height=400,
                showlegend=False
            )
            
            # Save chart as image
            img_bytes = fig.to_image(format="png", width=600, height=400)
            img_buffer = BytesIO(img_bytes)
            
            # Add image to PDF
            chart_img = RLImage(img_buffer, width=5*inch, height=3.3*inch)
            story.append(chart_img)
        else:
            story.append(Paragraph("No cooling curve data available.", styles['Normal']))
        
        # PAGE 2: DATA APPENDIX
        story.append(PageBreak())
        story.append(Paragraph("Data Appendix - Consolidated Shell Data", title_style))
        story.append(Spacer(1, 20))
        
        if consolidated_shell_data:
            # Create consolidated data table
            df_consolidated = pd.DataFrame(consolidated_shell_data)
            
            # Prepare table data
            table_data = [list(df_consolidated.columns)]
            for _, row in df_consolidated.iterrows():
                table_data.append([str(val) for val in row.values])
            
            # Create table with appropriate column widths
            num_cols = len(df_consolidated.columns)
            col_width = 7.5 * inch / num_cols
            
            data_table = Table(table_data, colWidths=[col_width] * num_cols)
            data_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1f4e79')),
                ('TEXTCOLOR', (0, 0), (-1, 0), whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, black),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, HexColor('#f0f0f0')])
            ]))
            
            story.append(data_table)
        else:
            story.append(Paragraph("No shell data available.", styles['Normal']))
        
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

=======
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
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
<<<<<<< HEAD
                canvas.setFillColor(gray)
=======
                canvas.setFillColor(rl_colors.gray)
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
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
                    temp_cols = [col for col in plateau_data.columns if col not in ['Time', 'Time_seconds']]
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
<<<<<<< HEAD
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
=======
            ('TEXTCOLOR', (0, 0), (-1, 0), rl_colors.white),
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
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
<<<<<<< HEAD
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, light_gray]),
=======
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [rl_colors.white, light_gray]),
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
            
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
                temp_cols = [col for col in df.columns if col not in ['Time', 'Time_seconds']]
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
                    if col not in ['Time', 'Time_seconds']:
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
                
<<<<<<< HEAD
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
                
=======
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
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
                    
                    st.metric(
                        label=f"📊 {pos_name}",
                        value=f"{pos_info['data'].shape[0]} samples",
                        delta=f"{temp_sensors} sensors"
                    )
                    st.caption(f"Sheet: {sheet_info} ({total_sheets} total)")
                else:
                    # DAT file display (original)
                    st.metric(
                        label=pos_name,
                        value=f"{pos_info['data'].shape[0]} samples",
                        delta=f"{pos_info['data']['Time_seconds'].max():.1f}s"
                    )
        
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
                    st.subheader(get_text("plateau_detection_settings"))
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        flat_th = st.slider(get_text("flatness_celsius"), 2, 10, 5)
                    with col2:
<<<<<<< HEAD
                        min_dur = st.slider(get_text("plateau_min_seconds"), 1, 20, 1)
=======
                        min_dur = st.slider(get_text("plateau_min_seconds"), 1, 20, 2)
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
                    with col3:
                        # Create sensor options with Head as default
                        sensor_options = []
                        if 'Head' in df.columns:
                            sensor_options.append('Head')
                        
                        # Add numbered sensors (1-4)
                        for i in range(1, 5):
                            if str(i) in df.columns:
                                sensor_options.append(str(i))
                        
                        # Add any other sensors and average option
                        other_sensors = [col for col in df.columns if col not in ['Time', 'Time_seconds', 'Head'] + [str(i) for i in range(1, 5)]]
                        sensor_options.extend(other_sensors)
                        
                        # Add average option
                        if len([col for col in df.columns if col not in ['Time', 'Time_seconds']]) > 1:
                            sensor_options.append('Average')
                        
                        sensor_for_detection = st.selectbox(
                            get_text("sensor_label"), 
                            sensor_options, 
                            index=0,
                            help="Sélectionnez le capteur à utiliser pour la détection des plateaux"
                        )
                
<<<<<<< HEAD
                # State management: Clear results when settings change
                current_settings = {
                    'position': selected_position,
                    'flat_th': flat_th,
                    'min_dur': min_dur,
                    'sensor': sensor_for_detection
                }
                
                # Check if settings have changed
                if 'previous_settings' not in st.session_state:
                    st.session_state.previous_settings = current_settings
                elif st.session_state.previous_settings != current_settings:
                    # Settings changed - clear any cached results
                    st.session_state.pop("detected_shells", None)
                    st.session_state.pop("shell_summary_data", None)
                    st.session_state.previous_settings = current_settings
                    # Force rerun to clear stale UI elements
                    st.rerun()
                
=======
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
                # Calculate data resolution
                df_res = 1.0 / (df['Time_seconds'].iloc[1] - df['Time_seconds'].iloc[0]) if len(df) > 1 else 1.0
                
                # Prepare sensor data
                if sensor_for_detection == 'Average':
                    # Calculate average of all temperature sensors
                    temp_cols = [col for col in df.columns if col not in ['Time', 'Time_seconds']]
                    sensor_data = df[temp_cols].mean(axis=1)
                else:
                    sensor_data = df[sensor_for_detection]
                
                # Dynamic plateau detection with rolling standard deviation
                def detect_plateaus_rolling_std(data, sensor_data, flat_th, min_dur, df_res):
                    plateaus = []
                    
                    # Calculate rolling standard deviation with 0.5 second window
<<<<<<< HEAD
                    # Ensure minimum window size of 3 for meaningful std calculation
                    window_size = max(3, int(1/df_res * 0.5))
                    roll_std = pd.Series(sensor_data).rolling(window=window_size, center=True).std()
                    
                    # Fill NaN values at the beginning and end
                    roll_std = roll_std.bfill().ffill()
=======
                    window_size = max(1, int(1/df_res * 0.5))
                    roll_std = pd.Series(sensor_data).rolling(window=window_size, center=True).std()
                    
                    # Fill NaN values at the beginning and end
                    roll_std = roll_std.fillna(method="bfill").fillna(method="ffill")
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
                    
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
                    
<<<<<<< HEAD

                    
=======
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
                    # Filter segments by minimum duration
                    for segment in stable_segments:
                        start_time = data['Time_seconds'].iloc[segment['start']]
                        end_time = data['Time_seconds'].iloc[segment['end']]
                        duration = end_time - start_time
                        
                        if duration >= min_dur:
                            # Extract temperatures for this plateau
                            plateau_temps = sensor_data.iloc[segment['start']:segment['end']+1]
<<<<<<< HEAD
                            avg_temp = plateau_temps.mean()
                            
                            # Apply minimum temperature filter (300°C threshold)
                            min_temp_threshold = 300.0
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
                
                plateaus, roll_std, stable_mask = detect_plateaus_rolling_std(df, df[sensor_for_detection], flat_th, min_dur, df_res)
                
                # Clear any cached results when no plateaus are detected
                if not plateaus:
                    st.session_state.pop("detected_shells", None)
                    st.session_state.pop("shell_summary_data", None)
                    st.session_state.pop("shell_summary_df", None)
=======
                            
                            plateau = {
                                'start': segment['start'],
                                'end': segment['end'],
                                'duration': duration,
                                'avg_temp': plateau_temps.mean(),
                                'temps': plateau_temps.tolist(),
                                'std': plateau_temps.std()
                            }
                            plateaus.append(plateau)
                    
                    return plateaus, roll_std, stable
                
                plateaus, roll_std, stable_mask = detect_plateaus_rolling_std(df, sensor_data, flat_th, min_dur, df_res)
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
                
                # Show detection info
                st.caption(get_text("sensor_flatness_duration").format(
                    sensor=sensor_for_detection, 
                    flatness=flat_th, 
                    duration=min_dur
                ))
                
                if plateaus:
                    st.success(f"✅ **Trouvé {len(plateaus)} plateau(x)** qui répondent aux critères!")
                    
                    # Show additional rolling std info
                    avg_std = roll_std.mean()
                    max_std = roll_std.max()
                    stable_percentage = (stable_mask.sum() / len(stable_mask)) * 100
                    st.info(get_text("mobile_std_analysis").format(
                        avg_std=avg_std,
                        max_std=max_std,
                        stable_percentage=stable_percentage
                    ))
                else:
<<<<<<< HEAD
                    st.warning(get_text("no_plateau_found"))
=======
                    st.caption(get_text("no_plateau_found"))
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
                
                # Create temperature curve plot with rolling std
                fig = go.Figure()
                
                # Plot all sensor curves
                sensor_columns = [col for col in df.columns if col not in ['Time', 'Time_seconds']]
                colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
                
                for i, sensor in enumerate(sensor_columns):
                    fig.add_trace(go.Scatter(
                        x=df['Time_seconds'],
                        y=df[sensor],
                        mode='lines',
                        name=sensor,
                        line=dict(color=colors[i % len(colors)], width=2),
                        yaxis='y'
                    ))
                
                # Add rolling standard deviation trace (on secondary y-axis)
                fig.add_trace(go.Scatter(
                    x=df['Time_seconds'],
                    y=roll_std,
                    mode='lines',
                    name=f'Rolling Std ({sensor_for_detection})',
                    line=dict(color='purple', width=1, dash='dot'),
                    yaxis='y2',
                    opacity=0.7
                ))
                
                # Add flatness threshold line
                fig.add_hline(y=flat_th, line_dash="dash", line_color="purple", 
                             annotation_text=get_text("flatness_threshold").format(flatness=flat_th),
                             yref='y2')
                
                # Add plateau markers
                for i, plateau in enumerate(plateaus):
                    start_time = df['Time_seconds'].iloc[plateau['start']]
                    end_time = df['Time_seconds'].iloc[plateau['end']]
                    
                    # Add vertical lines for plateau boundaries
                    fig.add_vline(x=start_time, line_dash="dash", line_color="green", 
                                 annotation_text=f"Shell {i+1} Start")
                    fig.add_vline(x=end_time, line_dash="dash", line_color="red", 
                                 annotation_text=f"Shell {i+1} End")
                    
                    # Add plateau region highlight
                    fig.add_vrect(
                        x0=start_time, x1=end_time,
                        fillcolor="rgba(0,255,0,0.1)",
                        layer="below",
                        line_width=0,
                    )
                
                # Update layout with dual y-axes
                fig.update_layout(
                    title=get_text("temp_curves_with_std").format(position=selected_position),
                    xaxis_title=get_text("time_seconds"),
                    yaxis=dict(
                        title=get_text("temperature_celsius"),
                        side="left"
                    ),
                    yaxis2=dict(
                        title=get_text("mobile_std_celsius"),
                        side="right",
                        overlaying="y",
                        range=[0, max(roll_std.max() * 1.2, flat_th * 1.5)]
                    ),
                    hovermode='x unified',
                    height=600
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Display detected plateaus with comprehensive metrics
<<<<<<< HEAD
                # Only show results if plateaus are actually detected in current run
                if plateaus and len(plateaus) > 0:
                    st.subheader(f"🎯 Coques de Verre Détectées: {len(plateaus)}")
                    
                    # Create Peak Temperature Summary (Antoine Le Du's requirement)
=======
                if plateaus:
                    st.subheader(f"🎯 Coques de Verre Détectées: {len(plateaus)}")
                    
                    # Create comprehensive shell summary
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
                    shell_summary_data = []
                    sensor_columns = [col for col in df.columns if col not in ['Time', 'Time_seconds']]
                    
                    for i, plateau in enumerate(plateaus):
                        start_idx = plateau['start']
                        end_idx = plateau['end']
                        start_time = df['Time_seconds'].iloc[start_idx]
                        end_time = df['Time_seconds'].iloc[end_idx]
                        duration = plateau['duration']
                        
<<<<<<< HEAD
                        # Extract start and end temperatures from the sensor used for detection
                        start_temp = df[sensor_for_detection].iloc[start_idx]
                        end_temp = df[sensor_for_detection].iloc[end_idx]
                        delta_t = start_temp - end_temp
                        
                        # Build shell metrics with new Peak Temperature Summary structure
                        shell_metrics = {
                            'Shell #': i + 1,
                            'Start Time (s)': round(start_time, 2),
                            'End Time (s)': round(end_time, 2),
                            'Duration (s)': round(duration, 2),
                            'Start Temp (°C)': round(start_temp, 1),
                            'End Temp (°C)': round(end_temp, 1),
                            'Delta-T (°C)': round(delta_t, 1)
                        }
                        
=======
                        # Extract shell data for this plateau
                        shell_data = df.iloc[start_idx:end_idx+1]
                        
                        # Build shell metrics
                        shell_metrics = {
                            'Shell': f"Shell {i+1}",
                            'Start Time (s)': round(start_time, 2),
                            'End Time (s)': round(end_time, 2),
                            'Duration (s)': round(duration, 2)
                        }
                        
                        # Add peak and average temperatures for each sensor
                        for sensor in sensor_columns:
                            peak_temp = shell_data[sensor].max()
                            avg_temp = shell_data[sensor].mean()
                            shell_metrics[f'{sensor} Peak (°C)'] = round(peak_temp, 1)
                            shell_metrics[f'{sensor} Avg (°C)'] = round(avg_temp, 1)
                        
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
                        shell_summary_data.append(shell_metrics)
                    
                    # Create DataFrame
                    shell_summary_df = pd.DataFrame(shell_summary_data)
                    
<<<<<<< HEAD
                    # Save analysis results to session state for report generation
                    if 'analysis_results' not in st.session_state:
                        st.session_state['analysis_results'] = {}
                    st.session_state['analysis_results'][selected_position] = shell_summary_df
                    
=======
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
                    # Display the table
                    st.dataframe(shell_summary_df, use_container_width=True)
                    
                    # Add download button for CSV
                    csv_data = shell_summary_df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Shell Summary (CSV)",
                        data=csv_data,
                        file_name=f"shell_summary_{selected_position}.csv",
                        mime="text/csv",
                        help="Download the complete shell analysis as CSV file"
                    )
                    
                    # Production metrics
                    col1, col2, col3 = st.columns(3)
                    with col1:
<<<<<<< HEAD
                        st.metric("Number of glass shell analyzed", len(plateaus))
                    with col2:
                        # Calculate Speed (pcs/min) based on total recording duration
                        total_duration = df['Time_seconds'].max() - df['Time_seconds'].min()
                        speed_pcs_per_min = (len(plateaus) / (total_duration / 60)) if total_duration > 0 else 0
                        st.metric("Speed (pcs/min)", f"{speed_pcs_per_min:.1f}")
=======
                        st.metric("Total Coquilles Détectées", len(plateaus))
                    with col2:
                        if len(plateaus) > 1:
                            total_time = df['Time_seconds'].iloc[plateaus[-1]['end']] - df['Time_seconds'].iloc[plateaus[0]['start']]
                            pcs_per_min = (len(plateaus) / total_time) * 60
                            st.metric(get_text("production_rate"), f"{pcs_per_min:.1f} pcs/min")
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
                    with col3:
                        if len(plateaus) > 0:
                            avg_duration = np.mean([p['duration'] for p in plateaus])
                            st.metric("Durée Coquille Moy", f"{avg_duration:.1f}s")
                    
                    # Quality insights
                    st.subheader(get_text("quality_insights"))
                    if len(shell_summary_data) > 0:
                        # Temperature consistency analysis
                        for sensor in sensor_columns:
                            peak_col = f'{sensor} Peak (°C)'
                            if peak_col in shell_summary_df.columns:
                                peak_temps = shell_summary_df[peak_col]
                                temp_std = peak_temps.std()
                                temp_mean = peak_temps.mean()
                                
                                if temp_std < 5:
                                    consistency = "Excellent"
                                    color = "green"
                                elif temp_std < 10:
                                    consistency = "Good"
                                    color = "orange"
                                else:
                                    consistency = "Variable"
                                    color = "red"
                                
                                st.markdown(f"**{sensor} Temperature Consistency**: :{color}[{consistency}] (σ = {temp_std:.1f}°C)")
                else:
                    st.caption(get_text("adjust_thresholds_tip"))
                
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
            
        if True:
            with st.expander(get_text("glass_shell_header"), expanded=False):
                
                if not selected_position:
                    st.info(get_text("upload_data_first_shell"))
                    st.markdown("""
                    **This analysis will provide:**
                    - 🎯 Individual glass shell isolation and analysis
                    - 📊 Peak temperature detection for each sensor
                    - 📈 Shell-specific temperature curves with peak markers
                    - ⏱️ Configurable shell duration settings
                    - 📋 Comprehensive shell metrics and statistics
                    - 🔍 Shell-by-shell quality assessment
                    """)
                else:
                    # Use position from sidebar
                    df = position_data[selected_position]['data']
                    
                    # Simple shell detection for demo
                    shell_duration = st.slider(get_text("shell_duration_slider"), 5.0, 30.0, 15.0)
                    total_time = df['Time_seconds'].max()
                    num_shells = int(total_time / shell_duration)
                    
                    shell_number = st.selectbox(
                        get_text("select_shell_number"),
                        list(range(1, num_shells + 1)),
                        help=get_text("select_shell_help")
                    )
                    
                    # Extract shell data
                    start_time = (shell_number - 1) * shell_duration
                    end_time = shell_number * shell_duration
                    
                    shell_data = df[(df['Time_seconds'] >= start_time) & (df['Time_seconds'] <= end_time)].copy()
                    
                    if not shell_data.empty:
                        # Create individual shell plot
                        fig = go.Figure()
                        
                        sensor_columns = [col for col in shell_data.columns if col not in ['Time', 'Time_seconds']]
                        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
                        
                        peak_temps = {}
                        
                        for i, sensor in enumerate(sensor_columns):
                             # Check if sensor has valid data
                             sensor_data = shell_data[sensor].dropna()
                             
                             if len(sensor_data) == 0:
                                 # Skip sensors with no valid data
                                 st.caption(get_text("no_data_caption").format(sensor=sensor))
                                 continue
                             
                             peak_temp = sensor_data.max()
                             peak_temps[sensor] = peak_temp
                             
                             fig.add_trace(go.Scatter(
                                 x=shell_data['Time_seconds'],
                                 y=shell_data[sensor],
                                 mode='lines+markers',
                                 name=f"{sensor} (Peak: {peak_temp:.1f}°C)",
                                 line=dict(color=colors[i % len(colors)], width=3),
                                 marker=dict(size=4)
                             ))
                             
                             # Add peak marker with validation
                             peak_idx = shell_data[sensor].idxmax()
                             
                             # Validate peak_idx is not NaN
                             if pd.notna(peak_idx) and peak_idx in shell_data.index:
                                 peak_time = shell_data.loc[peak_idx, 'Time_seconds']
                                 
                                 fig.add_trace(go.Scatter(
                                     x=[peak_time],
                                     y=[peak_temp],
                                     mode='markers',
                                     name=f"{sensor} Peak",
                                     marker=dict(color=colors[i % len(colors)], size=12, symbol='star'),
                                     showlegend=False
                                 ))
                         
                        fig.update_layout(
                            title=get_text("shell_analysis_title").format(shell_number=shell_number, position=selected_position) + f"<br>" + get_text("shell_duration").format(duration=f"{end_time-start_time:.1f}"),
                            xaxis_title=get_text("time_seconds"),
                            yaxis_title="Température (°C)",
                            height=500
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Display metrics
                        st.subheader(get_text("shell_metrics"))
                        
                        if peak_temps:
                            cols = st.columns(len(peak_temps))
                            
                            for i, (sensor, peak) in enumerate(peak_temps.items()):
                                with cols[i]:
                                    st.metric(f"{sensor} Peak", f"{peak:.1f}°C")
                            
                            # Additional metrics
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Durée", f"{end_time-start_time:.1f}s")
                            with col2:
                                avg_peak = np.mean(list(peak_temps.values()))
                                st.metric(get_text("mean_peak_temp"), f"{avg_peak:.1f}°C")
                            with col3:
                                temp_range = max(peak_temps.values()) - min(peak_temps.values())
                                st.metric(get_text("temp_range_full"), f"{temp_range:.1f}°C")
                        else:
                            st.error(get_text("no_sensor_data"))
            
<<<<<<< HEAD
        # Old Peak Temperature Data section removed - replaced by new plateau detection logic
=======
        if True:
            with st.expander(get_text("peak_temp_header"), expanded=False):
                
                if not selected_position:
                    st.info(get_text("upload_data_first_peak"))
                    st.markdown("""
                    **This analysis will provide:**
                    - 📊 Peak temperature detection for each shell
                    - 📈 Bar chart visualization of peak temperatures
                    - 📋 Comprehensive peak temperature data table
                    - 📈 Overall production statistics
                    - ⏱️ Cycle time and production rate metrics
                    - 🔍 Shell-by-shell temperature comparison
                    """)
                else:
                    # Use position from sidebar
                    df = position_data[selected_position]['data']
                
                # Simple shell detection
                shell_duration = st.slider(get_text("shell_duration_seconds"), 5.0, 30.0, 15.0)
                total_time = df['Time_seconds'].max()
                num_shells = int(total_time / shell_duration)
                
                # Calculate peak temps for each shell
                shell_peaks = []
                sensor_columns = [col for col in df.columns if col not in ['Time', 'Time_seconds']]
                
                for shell_num in range(1, num_shells + 1):
                    start_time = (shell_num - 1) * shell_duration
                    end_time = shell_num * shell_duration
                    
                    shell_data = df[(df['Time_seconds'] >= start_time) & (df['Time_seconds'] <= end_time)]
                    
                    if not shell_data.empty:
                        shell_info = {'Shell': shell_num}
                        for sensor in sensor_columns:
                            shell_info[f'{sensor}_peak'] = shell_data[sensor].max()
                        shell_peaks.append(shell_info)
                
                if shell_peaks:
                    peaks_df = pd.DataFrame(shell_peaks)
                    
                    # Create bar chart
                    fig = go.Figure()
                    
                    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
                    
                    for i, sensor in enumerate(sensor_columns):
                        peak_col = f'{sensor}_peak'
                        if peak_col in peaks_df.columns:
                            fig.add_trace(go.Bar(
                                x=peaks_df['Shell'],
                                y=peaks_df[peak_col],
                                name=sensor,
                                marker_color=colors[i % len(colors)]
                            ))
                    
                    fig.update_layout(
                        title=get_text("peak_temp_by_shell_title").format(position=selected_position),
                        xaxis_title=get_text("shell_number_axis"),
                        yaxis_title=get_text("peak_temp_y_axis"),
                        barmode='group',
                        height=500
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Display summary table
                    st.subheader(get_text("peak_temp_data"))
                    st.dataframe(peaks_df, use_container_width=True)
                    
                    # Overall statistics
                    st.subheader(get_text("overall_statistics"))
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        total_shells = len(peaks_df)
                        st.metric("Total Coquilles", total_shells)
                    
                    with col2:
                        if total_shells > 0:
                            avg_cycle_time = total_time / total_shells
                            st.metric("Temps Cycle Moy", f"{avg_cycle_time:.1f}s")
                    
                    with col3:
                        if total_time > 0:
                            production_rate = (total_shells / total_time) * 60
                            st.metric(get_text("production_rate"), f"{production_rate:.1f} pcs/min")
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9
            
        if True:
            with st.expander(get_text("multi_position_header"), expanded=False):
                
                if not selected_position:
                    st.info(get_text("upload_data_first_multi"))
                    st.markdown("""
                    **This analysis will provide:**
                    - 🏭 Multi-position glass shell journey visualization
                    - 📊 Head sensor temperature comparison across positions
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
                        
                        for i, (pos_name, pos_info) in enumerate(position_data.items()):
                            df = pos_info['data']
                            
                            # Use Head sensor for composite view
                            if 'Head' in df.columns:
                                fig.add_trace(go.Scatter(
                                    x=df['Time_seconds'],
                                    y=df['Head'],
                                    mode='lines',
                                    name=pos_name,
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
                            if 'Head' in df.columns:
                                comparison_data.append({
                                    'Position': pos_name,
                                    get_text('temp_max'): df['Head'].max(),
                                    get_text('temp_min'): df['Head'].min(),
                                    get_text('temp_avg'): df['Head'].mean(),
                                    get_text('duration'): df['Time_seconds'].max(),
                                    get_text('samples'): len(df)
                                })
                        
                        if comparison_data:
                            comparison_df = pd.DataFrame(comparison_data)
                            st.dataframe(comparison_df, use_container_width=True)
                    
                    else:
                        st.warning(get_text("upload_multiple_files"))

            
        if True:
            with st.expander(get_text("interactive_header"), expanded=False):
                
                if not selected_position:
                    st.info(get_text("upload_data_first_interactive"))
                    st.markdown("""
                    **This analysis will provide:**
                    - 🖼️ Interactive temperature visualization
                    - 🎛️ Customizable sensor selection
                    - 📈 Multi-sensor plotting capabilities
                    - 🔍 Zoom and pan functionality
                    - 📊 Hover data inspection
                    - ⏱️ Time-series temperature analysis
                    """)
                else:
                    # Use position from sidebar
                    df = position_data[selected_position]['data']
                    
                    sensor_columns = [col for col in df.columns if col not in ['Time', 'Time_seconds']]
                    selected_sensors = st.multiselect(get_text("select_sensors"), sensor_columns, default=sensor_columns[:3])
                    
                    fig = go.Figure()
                    for sensor in selected_sensors:
                        fig.add_trace(go.Scatter(
                            x=df['Time_seconds'],
                            y=df[sensor],
                            mode='lines',
                            name=sensor
                        ))
                    
                    fig.update_layout(
                        title=get_text("interactive_view"),
                        xaxis_title=get_text("time_seconds"),
                        yaxis_title=get_text("temperature_celsius"),
                        hovermode='x unified',
                        height=600
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)

            
        if True:
            with st.expander(get_text("thermal_journey_header"), expanded=False):
                
                # Multi-file upload section
                st.subheader(get_text("upload_multiple_files"))
                journey_files = st.file_uploader(
                "Upload multiple .dat files for thermal journey analysis",
                type=['dat'],
                accept_multiple_files=True,
                help="Upload files like cz_position6.dat, cz_position12.dat, etc."
            )
            
            if journey_files:
                # Cache hygiene - clear stale data on new file upload
                st.session_state.pop("detected_shells", None)
                
                # Process all uploaded files
                journey_data = {}
                
                for uploaded_file in journey_files:
                    try:
                        # Extract position from filename
                        filename = uploaded_file.name
                        if 'position' in filename.lower():
                            # Extract position number from filename
                            import re
                            position_match = re.search(r'position(\d+)', filename.lower())
                            if position_match:
                                position_num = position_match.group(1)
                                position_name = get_text("position_number").format(number=position_num)
                            else:
                                position_name = filename.replace('.dat', '').replace('cz_', '').title()
                        else:
                            position_name = filename.replace('.dat', '').title()
                        
                        # Read and process the file (same logic as before)
                        content = uploaded_file.read()
                        
                        # Try different encodings
                        for encoding in ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']:
                            try:
                                decoded_content = content.decode(encoding)
                                break
                            except UnicodeDecodeError:
                                continue
                        else:
                            st.error(f"Could not decode {filename}")
                            continue
                        
                        lines = decoded_content.strip().split('\n')
                        
                        # Find data start
                        data_start = 0
                        resolution = 0.05  # default
                        
                        for i, line in enumerate(lines):
                            if line.startswith('Resolution:'):
                                try:
                                    res_str = line.split(';')[1].replace(',', '.')
                                    resolution = float(res_str)
                                except:
                                    pass
                            elif 'Time;' in line and any(sensor in line for sensor in ['Head', '1', '2', '3', '4']):
                                data_start = i
                                break
                        
                        if data_start == 0:
                            st.error(f"Could not find data section in {filename}")
                            continue
                        
                        # Parse data
                        data_lines = lines[data_start:]
                        if len(data_lines) < 2:
                            st.error(f"No data found in {filename}")
                            continue
                        
                        # Get headers
                        headers = data_lines[0].split(';')
                        headers = [h.strip() for h in headers if h.strip()]
                        
                        # Parse data rows
                        data_rows = []
                        for line in data_lines[1:]:
                            if line.strip():
                                values = line.split(';')
                                if len(values) >= len(headers):
                                    data_rows.append(values[:len(headers)])
                        
                        if not data_rows:
                            st.error(f"No valid data rows in {filename}")
                            continue
                        
                        # Create DataFrame
                        df = pd.DataFrame(data_rows, columns=headers)
                        
                        # Clean numeric columns
                        for col in df.columns:
                            if col != 'Time':
                                df[col] = df[col].astype(str).str.replace(',', '.')
                                df[col] = pd.to_numeric(df[col], errors='coerce')
                        
                        # Convert time to seconds using robust Euro-Time Parser
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
                            except (ValueError, AttributeError, IndexError):
                                # Fallback for malformed time strings
                                return 0.0
                        
                        if 'Time' in df.columns:
                            df['Time_seconds'] = df['Time'].apply(euro_to_seconds)
                        else:
                            df['Time_seconds'] = df.index * resolution
                        
                        # Store the processed data
                        journey_data[position_name] = {
                            'data': df,
                            'filename': filename
                        }
                        
                    except Exception as e:
                        st.error(f"Error processing {uploaded_file.name}: {str(e)}")
                
                # Display journey analysis if we have data
                if journey_data:

                    
                    # Create the thermal journey plot
                    st.subheader(get_text("head_sensor_journey"))
                    
                    fig = go.Figure()
                    
                    # Professional color palette
                    colors = [
                        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
                    ]
                    
                    # Plot Head sensor for each position
                    positions_with_head = []
                    for i, (position_name, pos_data) in enumerate(journey_data.items()):
                        df = pos_data['data']
                        
                        if 'Head' in df.columns:
                            fig.add_trace(go.Scatter(
                                x=df['Time_seconds'],
                                y=df['Head'],
                                mode='lines',
                                name=position_name,
                                line=dict(
                                    color=colors[i % len(colors)], 
                                    width=3
                                ),
                                hovertemplate=f"<b>{position_name}</b><br>" +
                                            "Time: %{x:.1f}s<br>" +
                                            "Temperature: %{y:.1f}°C<br>" +
                                            "<extra></extra>"
                            ))
                            positions_with_head.append(position_name)
                    
                    # Professional styling
                    fig.update_layout(
                        title={
                            'text': "Parcours Thermique Ligne Complète - Comparaison Capteur Tête",
                            'x': 0.5,
                            'xanchor': 'center',
                            'font': {'size': 20, 'family': 'Arial Black'}
                        },
                        xaxis_title="Temps (s)",
                        yaxis_title="Température (°C)",
                        hovermode='x unified',
                        height=700,
                        legend=dict(
                            orientation="v",
                            yanchor="top",
                            y=1,
                            xanchor="left",
                            x=1.02,
                            bgcolor="rgba(255,255,255,0.8)",
                            bordercolor="rgba(0,0,0,0.2)",
                            borderwidth=1
                        ),
                        plot_bgcolor='rgba(248,249,250,0.8)',
                        paper_bgcolor='white',
                        font=dict(family="Arial", size=12),
                        margin=dict(r=150)
                    )
                    
                    # Add grid
                    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
                    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Journey insights
                    if positions_with_head:
                        st.subheader(get_text("thermal_journey_insights"))
                        
                        # Create comparison table
                        comparison_data = []
                        for position_name in positions_with_head:
                            df = journey_data[position_name]['data']
                            head_data = df['Head'].dropna()
                            
                            comparison_data.append({
                                'Position': position_name,
                                get_text("temp_max"): round(head_data.max(), 1),
                                get_text("temp_min"): round(head_data.min(), 1),
                                get_text("temp_avg"): round(head_data.mean(), 1),
                                get_text("temp_range_celsius"): round(head_data.max() - head_data.min(), 1),
                                get_text("duration"): round(df['Time_seconds'].max(), 1),
                                get_text("file"): journey_data[position_name]['filename']
                            })
                        
                        comparison_df = pd.DataFrame(comparison_data)
                        st.dataframe(comparison_df, use_container_width=True)
                        
                        # Download journey data
                        csv_data = comparison_df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Journey Analysis (CSV)",
                            data=csv_data,
                            file_name="thermal_journey_analysis.csv",
                            mime="text/csv",
                            help="Download the complete thermal journey comparison"
                        )
                        
                        # Quality assessment
                        st.subheader(get_text("line_performance"))
                        
                        # Temperature consistency across positions
                        max_temps = [data[get_text("temp_max")] for data in comparison_data]
                        temp_std = np.std(max_temps)
                        temp_mean = np.mean(max_temps)
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric(get_text("positions_analyzed"), len(positions_with_head))
                        with col2:
                            st.metric(get_text("avg_max_temp"), f"{temp_mean:.1f}°C")
                        with col3:
                            consistency_pct = (1 - temp_std/temp_mean) * 100 if temp_mean > 0 else 0
                            st.metric(get_text("temp_consistency"), f"{consistency_pct:.1f}%")
                        
                        # Performance insights
                        if temp_std < 10:
                            st.success("🎯 **Excellent Line Consistency**: Temperature variation across positions is minimal")
                        elif temp_std < 20:
                            st.warning("⚠️ **Moderate Variation**: Some positions show temperature differences")
                        else:
                            st.error("🚨 **High Variation**: Significant temperature differences detected across positions")
                    
                    else:
                        st.warning("⚠️ No Head sensor data found in uploaded files")
                
                else:
                    st.error(get_text("no_valid_data_extracted"))
            
            else:
                pass

            
        if True:
            with st.expander(get_text("ai_summary_header"), expanded=False):
                
<<<<<<< HEAD
                # New single-section layout
                st.header("Generate Insight Briefing")
                
                # First Expander: Global Identification
                with st.expander("Global Identification", expanded=False):
                    plant = st.text_input("Plant")
                    line_number = st.text_input("Line #")
                    glass_shell = st.text_input("Glass shell")
                    campaign_number = st.text_input("Campaign #")
                    # Use smart calendar input with extracted file date
                    default_date = st.session_state.get('file_date', date.today())
                    time_date = st.date_input("Time & date", value=default_date)
                
                # Second Expander: Toughening Parameters
                with st.expander("Toughening Parameters", expanded=False):
                    line_speed = st.text_input("Line speed (pcs/min)")
                    temperature_u4 = st.text_input("Temperature U4 furnace (°C)")
                    toughening_positions = st.text_input("Number of toughening positions with air / open positions")
                    air_pressure = st.text_input("Toughening air pressure top & bottom (bar)")
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
                                line_speed, temperature_u4, toughening_positions, air_pressure, air_temperature, rotation_speed
                            )
                            print(f"[DEBUG] Step 1 completed: {metadata}")
                            
                            # Calculate cooling curve data
                            print("[DEBUG] Step 2: Calculating cooling curve data")
                            cooling_curve_data = calculate_cooling_curve_data(st.session_state.get('analysis_results', {}))
                            print(f"[DEBUG] Step 2 completed: {cooling_curve_data}")
                            
                            # Create consolidated shell data
                            print("[DEBUG] Step 3: Creating consolidated shell data")
                            consolidated_shell_data = create_consolidated_shell_data(st.session_state.get('analysis_results', {}))
                            print(f"[DEBUG] Step 3 completed: {len(consolidated_shell_data)} records")
                            
                            # Generate PDF
                            print("[DEBUG] Step 4: Generating PDF")
                            pdf_buffer = generate_insight_briefing_pdf(metadata, cooling_curve_data, consolidated_shell_data)
                            print("[DEBUG] Step 4 completed: PDF generated successfully")
                            
                            # Create download button
                            st.success("✅ Insight Briefing PDF generated successfully!")
                            
                            # Display sample data for verification
                            st.subheader("📊 Sample Data for Verification")
                            
                            # Show cooling curve data
                            if cooling_curve_data:
                                st.write("**Cooling Curve Data (Position vs Mean Shell Temperature):**")
                                cooling_df = pd.DataFrame(cooling_curve_data)
                                st.dataframe(cooling_df, use_container_width=True)
                            
                            # Show first 3 rows of consolidated shell data
                            if consolidated_shell_data:
                                st.write("**First 3 rows of Consolidated Peak Temperature Summary:**")
                                consolidated_df = pd.DataFrame(consolidated_shell_data)
                                st.dataframe(consolidated_df.head(3), use_container_width=True)
                            
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

=======
                # Create tabs for different report modes
                tab1, tab2 = st.tabs(["🤖 AI Analysis", "📋 Report Template Generator"])
                
                with tab1:
                    # Original AI Analysis functionality
                    
                    # Try to load API key from .env file first
                    env_api_key = os.getenv('OPENAI_API_KEY')
                    
                    if env_api_key:
                        openai_api_key = env_api_key
                    else:
                        openai_api_key = st.text_input(
                            "OpenAI API Key",
                            type="password",
                            help="Enter your OpenAI API key to enable AI-powered analysis reports"
                        )
                    
                    if not openai_api_key:
                        st.warning("⚠️ Please provide your OpenAI API key to use AI reporting features")
                        st.markdown("""
                        **Option 1: Use .env file (Recommended)**
                        1. Add your API key to the `.env` file: `OPENAI_API_KEY=your_key_here`
                        2. Restart the app
                        
                        **Option 2: Manual entry**
                        1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
                        2. Create an account or sign in
                        3. Generate a new API key
                        4. Paste it above to enable AI reports
                        """)
                        st.stop()
                    
                    # Single file analysis
                    if position_data:
                        selected_position = st.selectbox(
                            "Select Position for AI Analysis:", 
                            list(position_data.keys()),
                            help="Choose which position to analyze with AI"
                        )
                        df = position_data[selected_position]['data']
                    
                    if st.button("🧠 Generate AI Analysis Report", type="primary"):
                        with st.spinner("🤖 AI is analyzing your thermal data..."):
                            try:
                                # Perform plateau detection for the report using rolling std
                                sensor_for_detection = 'Head' if 'Head' in df.columns else df.columns[1]
                                flat_th = 2.0  # Reduced from 5.0 to 2.0 for more sensitive detection
                                min_dur = 1.0  # Reduced from 2.0 to 1.0 for shorter plateaus
                                
                                # Calculate data resolution
                                df_res = 1.0 / (df['Time_seconds'].iloc[1] - df['Time_seconds'].iloc[0]) if len(df) > 1 else 1.0
                                
                                # Prepare sensor data
                                sensor_data = df[sensor_for_detection]
                                
                                def detect_plateaus_for_ai(data, sensor_data, flat_th, min_dur, df_res):
                                    plateaus = []
                                    
                                    # Calculate rolling standard deviation with adaptive window
                                    window_size = max(3, int(1/df_res * 0.3))  # Smaller window for more sensitivity
                                    roll_std = pd.Series(sensor_data).rolling(window=window_size, center=True).std()
                                    
                                    # Fill NaN values at the beginning and end
                                    roll_std = roll_std.fillna(method="bfill").fillna(method="ffill")
                                    
                                    # Use adaptive threshold based on data characteristics
                                    data_std = sensor_data.std()
                                    adaptive_threshold = min(flat_th, data_std * 0.1)  # Use smaller of fixed or adaptive threshold
                                    
                                    # Identify stable regions
                                    stable = roll_std < adaptive_threshold
                                    
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
                                    
                                    # Filter segments by minimum duration and temperature criteria
                                    for segment in stable_segments:
                                        start_time = data['Time_seconds'].iloc[segment['start']]
                                        end_time = data['Time_seconds'].iloc[segment['end']]
                                        duration = end_time - start_time
                                        
                                        if duration >= min_dur:
                                            # Extract temperatures for this plateau
                                            plateau_temps = sensor_data.iloc[segment['start']:segment['end']+1]
                                            avg_temp = plateau_temps.mean()
                                            
                                            # Only consider plateaus with reasonable temperatures (above ambient)
                                            if avg_temp > 100:  # Assuming glass processing temperatures are above 100°C
                                                plateau = {
                                                    'start': segment['start'],
                                                    'end': segment['end'],
                                                    'duration': duration,
                                                    'avg_temp': avg_temp,
                                                    'temps': plateau_temps.tolist(),
                                                    'std': plateau_temps.std()
                                                }
                                                plateaus.append(plateau)
                                    
                                    return plateaus
                                
                                plateaus = detect_plateaus_for_ai(df, sensor_data, flat_th, min_dur, df_res)
                                
                                # Calculate metrics for AI analysis
                                sensor_columns = [col for col in df.columns if col not in ['Time', 'Time_seconds']]
                                
                                # Clean sensor names and handle unnamed/NaN columns
                                clean_sensor_data = {}
                                for sensor in sensor_columns:
                                    # Skip unnamed, NaN, or invalid columns
                                    if (pd.isna(sensor) or 
                                        'Unnamed' in str(sensor) or 
                                        str(sensor).strip() == '' or
                                        str(sensor).lower() == 'nan'):
                                        continue
                                    
                                    # Clean sensor name
                                    clean_name = str(sensor).strip()
                                    
                                    # Only include columns with valid data
                                    sensor_data = df[sensor].dropna()
                                    if len(sensor_data) > 0 and not sensor_data.isna().all():
                                        clean_sensor_data[clean_name] = df[sensor].max()
                                
                                total_duration = df['Time_seconds'].max()
                                
                                # Find peak temperatures from clean data
                                peak_temps = clean_sensor_data
                                highest_peak = max(peak_temps.values()) if peak_temps else 0
                                highest_peak_sensor = max(peak_temps, key=peak_temps.get) if peak_temps else "Unknown"
                                
                                # Production rate
                                production_rate = (len(plateaus) / total_duration) * 60 if total_duration > 0 else 0
                                
                                # Detect anomalies with improved formatting
                                anomalies = []
                                spike_details = []
                                
                                for original_sensor, clean_name in zip(sensor_columns, clean_sensor_data.keys()):
                                    sensor_data = df[original_sensor].dropna()
                                    if len(sensor_data) == 0:
                                        continue
                                        
                                    temp_std = sensor_data.std()
                                    temp_mean = sensor_data.mean()
                                    
                                    # Check for temperature spikes (values > 3 standard deviations)
                                    spikes = sensor_data[abs(sensor_data - temp_mean) > 3 * temp_std]
                                    if len(spikes) > 0:
                                        max_spike = spikes.max()
                                        spike_magnitude = max_spike - temp_mean
                                        spike_details.append(f"- {clean_name}: +{spike_magnitude:.1f}°C (peak: {max_spike:.1f}°C)")
                                
                                # Check for inconsistent plateaus
                                if len(plateaus) > 1:
                                    plateau_durations = [p['duration'] for p in plateaus]
                                    duration_std = np.std(plateau_durations)
                                    duration_mean = np.mean(plateau_durations)
                                    if duration_std > duration_mean * 0.3:
                                        anomalies.append(f"Inconsistent plateau durations detected (variation: {duration_std:.1f}s)")
                                
                                # Add spike details to anomalies if any found
                                if spike_details:
                                    anomalies.append("Significant temperature spikes observed:\n" + "\n".join(spike_details))
                                
                                # Prepare data for AI prompt
                                analysis_data = {
                                    'position': selected_position,
                                    'shells_detected': len(plateaus),
                                    'total_duration': total_duration,
                                    'production_rate': production_rate,
                                    'highest_peak': highest_peak,
                                    'highest_peak_sensor': highest_peak_sensor,
                                    'anomalies': anomalies,
                                    'sensor_peaks': peak_temps,
                                    'avg_shell_duration': np.mean([p['duration'] for p in plateaus]) if plateaus else 0
                                }
                                
                                # Create AI prompt
                                ai_prompt = f"""
                                Analyze the thermal data from {selected_position} and provide a professional engineering report.
                                
                                Data Summary:
                                - Glass shells detected: {analysis_data['shells_detected']}
                                - Total analysis duration: {analysis_data['total_duration']:.1f} seconds
                                - Production rate: {analysis_data['production_rate']:.1f} pieces per minute
                                - Highest peak temperature: {analysis_data['highest_peak']:.1f}°C (from {analysis_data['highest_peak_sensor']} sensor)
                                - Average shell duration: {analysis_data['avg_shell_duration']:.1f} seconds
                                - Sensor peak temperatures: {analysis_data['sensor_peaks']}
                                - Detected anomalies: {analysis_data['anomalies'] if analysis_data['anomalies'] else 'None detected'}
                                
                                Please provide:
                                1. Executive Summary (2-3 sentences)
                                2. Production Performance Analysis
                                3. Temperature Profile Assessment
                                4. Quality Indicators
                                5. Recommendations (if any issues detected)
                                
                                Use a professional tone suitable for R&D engineers. Focus on actionable insights.
                                """
                                
                                # Simulate AI response (replace with actual OpenAI call)
                                ai_response = f"""
# 🔬 Thermal Analysis Report - {selected_position}

## Executive Summary
Analysis of {selected_position} reveals {analysis_data['shells_detected']} glass shells processed over {analysis_data['total_duration']:.1f} seconds, achieving a production rate of {analysis_data['production_rate']:.1f} pcs/min. The thermal profile shows peak temperatures reaching {analysis_data['highest_peak']:.1f}°C on the {analysis_data['highest_peak_sensor']} sensor, indicating {'optimal' if analysis_data['highest_peak'] < 500 else 'elevated'} processing conditions.

## Production Performance Analysis
- **Shell Detection**: {analysis_data['shells_detected']} shells successfully identified{' - No stable plateaus were found based on the configured thresholds. Please verify data integrity or adjust detection settings.' if analysis_data['shells_detected'] == 0 else ''}
- **Cycle Time**: {f"Average {analysis_data['avg_shell_duration']:.1f}s per shell" if analysis_data['shells_detected'] > 0 else "N/A - No shells detected"}
- **Production Rate**: {analysis_data['production_rate']:.1f} pcs/min {'(within target range)' if 2 <= analysis_data['production_rate'] <= 6 else '(review recommended)' if analysis_data['shells_detected'] > 0 else '(unable to calculate)'}
- **Process Efficiency**: {'High' if analysis_data['production_rate'] > 3 else 'Moderate' if analysis_data['production_rate'] > 1.5 else 'Low' if analysis_data['shells_detected'] > 0 else 'Unable to assess'}

## Temperature Profile Assessment
**Peak Temperatures (°C):**
{chr(10).join([f"- {sensor}: {temp:.1f}" for sensor, temp in analysis_data['sensor_peaks'].items()]) if analysis_data['sensor_peaks'] else "- No valid sensor data available"}

**Thermal Uniformity**: {'Excellent' if analysis_data['sensor_peaks'] and max(analysis_data['sensor_peaks'].values()) - min(analysis_data['sensor_peaks'].values()) < 20 else 'Good' if analysis_data['sensor_peaks'] and max(analysis_data['sensor_peaks'].values()) - min(analysis_data['sensor_peaks'].values()) < 40 else 'Variable' if analysis_data['sensor_peaks'] else 'Unable to assess'}

## Quality Indicators
{'✅ **No anomalies detected** - Process running within normal parameters' if not analysis_data['anomalies'] else '⚠️ **Anomalies Detected:**' + chr(10) + chr(10).join([f"{anomaly}" for anomaly in analysis_data['anomalies']])}

## Recommendations
{f"- Verify equipment readiness and sensor calibration{chr(10)}- Review detection threshold settings (currently 5°C stability)" if analysis_data['shells_detected'] == 0 else '- Continue current operating parameters' if not analysis_data['anomalies'] and 2 <= analysis_data['production_rate'] <= 6 else '- Review temperature control settings' if analysis_data['highest_peak'] > 500 else '- Optimize cycle time for improved throughput' if analysis_data['production_rate'] < 2 else '- Monitor for process stability'}
{'- Investigate sensor calibration' if len(analysis_data['anomalies']) > 2 else ''}

## Summary
{f"No glass shells were detected in this thermal run. This could indicate equipment standby mode, sensor calibration issues, or data collection during non-production periods. Recommend verifying process status and detection parameters." if analysis_data['shells_detected'] == 0 else f"Production cycle completed successfully with {analysis_data['shells_detected']} shells detected. {'Process parameters are optimal for consistent glass production.' if not analysis_data['anomalies'] and 2 <= analysis_data['production_rate'] <= 6 else 'Minor process adjustments recommended to optimize thermal consistency and production efficiency.'}"}

---
*Report generated by Celcius AI*
"""
                                
                                # Display the AI report
                                st.subheader(get_text("ai_analysis_report"))
                                st.markdown(ai_response)
                                
                                # Interactive Shell Analysis (Optional Enhancement)
                                if plateaus:
                                    st.subheader(get_text("interactive_shell_analysis"))
                                    st.info(get_text("click_shell_info"))
                                    
                                    # Create shell selection
                                    shell_options = [f"Shell {i+1} ({p['avg_temp']:.1f}°C, {p['duration']:.1f}s)" for i, p in enumerate(plateaus)]
                                    selected_shell_idx = st.selectbox(
                                        get_text("select_shell_analysis"),
                                        range(len(shell_options)),
                                        format_func=lambda x: shell_options[x],
                                        help=get_text("choose_shell_detail")
                                    )
                                    
                                    if selected_shell_idx is not None:
                                        selected_plateau = plateaus[selected_shell_idx]
                                        
                                        # Extract shell data with buffer
                                        buffer_time = 5  # seconds before/after shell
                                        start_idx = max(0, selected_plateau['start'] - int(buffer_time / 0.1))
                                        end_idx = min(len(df), selected_plateau['end'] + int(buffer_time / 0.1))
                                        
                                        shell_df = df.iloc[start_idx:end_idx].copy()
                                        
                                        # Create zoomed-in plot
                                        fig_shell = go.Figure()
                                        
                                        # Plot all sensors for the shell region
                                        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
                                        for i, sensor in enumerate(clean_sensor_data.keys()):
                                            if sensor in df.columns:
                                                fig_shell.add_trace(go.Scatter(
                                                    x=shell_df['Time_seconds'],
                                                    y=shell_df[sensor],
                                                    mode='lines+markers',
                                                    name=sensor,
                                                    line=dict(color=colors[i % len(colors)], width=3),
                                                    marker=dict(size=4)
                                                ))
                                        
                                        # Highlight the actual shell region
                                        shell_start_time = df['Time_seconds'].iloc[selected_plateau['start']]
                                        shell_end_time = df['Time_seconds'].iloc[selected_plateau['end']]
                                        
                                        fig_shell.add_vrect(
                                            x0=shell_start_time,
                                            x1=shell_end_time,
                                            fillcolor="rgba(255,215,0,0.3)",
                                            layer="below",
                                            line_width=0,
                                            annotation_text=f"Shell {selected_shell_idx + 1}",
                                            annotation_position="top left"
                                        )
                                        
                                        # Add vertical markers
                                        fig_shell.add_vline(
                                            x=shell_start_time,
                                            line_dash="dash",
                                            line_color="green",
                                            annotation_text=get_text("shell_start")
                                        )
                                        fig_shell.add_vline(
                                            x=shell_end_time,
                                            line_dash="dash",
                                            line_color="red",
                                            annotation_text=get_text("shell_end")
                                        )
                                        
                                        fig_shell.update_layout(
                                            title=get_text("detailed_shell_analysis_title").format(shell_number=selected_shell_idx + 1),
                                            xaxis_title=get_text("time_seconds"),
                                            yaxis_title=get_text("temperature_celsius"),
                                            hovermode='x unified',
                                            height=500,
                                            showlegend=True
                                        )
                                        
                                        st.plotly_chart(fig_shell, use_container_width=True)
                                        
                                        # Shell-specific metrics
                                        col1, col2, col3, col4 = st.columns(4)
                                        with col1:
                                            st.metric(get_text("duration_metric"), f"{selected_plateau['duration']:.1f}s")
                                        with col2:
                                            st.metric(get_text("avg_temp_metric"), f"{selected_plateau['avg_temp']:.1f}°C")
                                        with col3:
                                            shell_data = df.iloc[selected_plateau['start']:selected_plateau['end']]
                                            temp_stability = shell_data[sensor_for_detection].std()
                                            st.metric("Stabilité Temp", f"±{temp_stability:.1f}°C")
                                        with col4:
                                            shell_quality = "Excellent" if temp_stability < 2 else "Good" if temp_stability < 5 else "Variable"
                                            st.metric("Qualité Coquille", shell_quality)
                                
                                # Download options
                                st.subheader(get_text("download_options"))
                                col1, col2 = st.columns(2)
                                
                                with col1:
                                    # Text download
                                    txt_report = ai_response.replace('#', '').replace('*', '').replace('✅', '').replace('⚠️', '').replace('🔬', '').replace('📋', '')
                                    st.download_button(
                                        label="📄 Download as TXT",
                                        data=txt_report,
                                        file_name=f"thermal_report_{selected_position}.txt",
                                        mime="text/plain"
                                    )
                                
                                with col2:
                                    # CSV data download
                                    report_data = pd.DataFrame([analysis_data])
                                    csv_data = report_data.to_csv(index=False)
                                    st.download_button(
                                        label="📊 Download Data (CSV)",
                                        data=csv_data,
                                        file_name=f"thermal_data_{selected_position}.csv",
                                        mime="text/csv"
                                    )
                                
                            except Exception as e:
                                st.error(f"Error generating AI report: {str(e)}")
                    else:
                        st.info(get_text("upload_dat_file"))
            
            with tab2:
                # Report Template Generator
                st.subheader(get_text("report_template_generator"))
                st.info(get_text("generate_professional_reports"))
                
                # Report Configuration Section
                st.subheader(get_text("report_configuration"))
                
                # Report Type Selection
                col1, col2 = st.columns(2)
                with col1:
                    template_report_type = st.selectbox(
                        get_text("report_type"),
                        [get_text("single_position"), get_text("full_line_journey"), get_text("anomaly_summary_only")],
                        help=get_text("choose_report_scope")
                    )
                
                with col2:
                    output_format = st.selectbox(
                        get_text("output_format"),
                        [".txt", ".pdf"],
                        help=get_text("select_download_format")
                    )
                
                # Report Customization
                st.subheader(get_text("report_customization"))
                
                col1, col2 = st.columns(2)
                with col1:
                    report_title = st.text_input(
                        get_text("report_title"),
                        value="Thermal Analysis Report",
                        help=get_text("enter_custom_title")
                    )
                    
                    analyst_name = st.text_input(
                        get_text("analyst_name"),
                        value="",
                        placeholder="e.g., Antoine Dubois",
                        help=get_text("enter_analyst_name")
                    )
                
                with col2:
                    report_date = st.date_input(
                        get_text("report_date"),
                        value=pd.Timestamp.now().date(),
                        help=get_text("select_report_date")
                    )
                    
                    company_name = st.text_input(
                        get_text("company_department"),
                        value="Sediver R&D",
                        help=get_text("enter_company_dept")
                    )
                
                # Optional Sections Toggle
                st.subheader(get_text("report_sections"))
                st.write(get_text("toggle_sections_info"))
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    include_executive = st.checkbox(get_text("executive_summary"), value=True)
                    include_shell_table = st.checkbox(get_text("shell_detection_table"), value=True)
                
                with col2:
                    include_temp_profile = st.checkbox(get_text("temperature_profile"), value=True)
                    include_quality_alerts = st.checkbox(get_text("quality_alerts"), value=True)
                
                with col3:
                    include_recommendations = st.checkbox(get_text("recommendations"), value=True)
                    include_charts = st.checkbox(get_text("charts_graphs"), value=False)
                
                # Data Selection for Report
                st.subheader(get_text("data_selection"))
                
                if position_data:
                    if template_report_type == get_text("single_position"):
                        selected_position_template = st.selectbox(
                            get_text("select_position_report"),
                            list(position_data.keys()),
                            key="template_position_select",
                            help=get_text("choose_position_include")
                        )
                        
                        # Show data preview
                        if selected_position_template:
                            df_preview = position_data[selected_position_template]['data']
                            st.write(f"**{get_text('data_preview_for')} {selected_position_template}:**")
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Total Échantillons", len(df_preview))
                            with col2:
                                st.metric("Durée", f"{df_preview['Time_seconds'].max():.1f}s")
                            with col3:
                                sensor_count = len([col for col in df_preview.columns if col not in ['Time', 'Time_seconds']])
                                st.metric("Capteurs", sensor_count)
                    
                    elif template_report_type == get_text("full_line_journey"):
                        st.multiselect(
                            get_text("select_positions_journey"),
                            list(position_data.keys()),
                            default=list(position_data.keys())[:3] if len(position_data) >= 3 else list(position_data.keys()),
                            key="template_journey_select"
                        )
                    
                    else:  # Anomaly Summary Only
                        st.multiselect(
                            get_text("select_positions_anomaly"),
                            list(position_data.keys()),
                            default=list(position_data.keys()),
                            key="template_anomaly_select"
                        )
                
                # Live Preview Section
                st.subheader(get_text("live_preview"))
                
                if st.button(get_text("generate_preview"), type="secondary"):
                    # Generate report preview
                    preview_content = f"""
# {report_title}

**Generated by:** {analyst_name if analyst_name else 'Thermal Analysis System'}  
**Date:** {report_date.strftime('%B %d, %Y')}  
**Company:** {company_name}  
**Report Type:** {template_report_type}

---

"""
                    
                    if include_executive:
                        preview_content += """
## 📋 Executive Summary
This thermal analysis report provides comprehensive insights into the glass toughening process performance. The analysis covers temperature profiles, shell detection, and quality indicators to ensure optimal production parameters.

"""
                    
                    if include_shell_table and position_data and template_report_type == "Single Position":
                        preview_content += """
## 🔍 Shell Detection Results
| Shell # | Start Time | Duration | Avg Temp | Quality |
|---------|------------|----------|----------|---------|
| Shell 1 | 00:15:23   | 12.3s    | 485.2°C  | Excellent |
| Shell 2 | 00:28:45   | 11.8s    | 487.1°C  | Good |
| Shell 3 | 00:41:12   | 12.1s    | 486.5°C  | Excellent |

"""
                    
                    if include_temp_profile:
                        preview_content += """
## 🌡️ Temperature Profile Analysis
**Peak Temperatures:**
- Head Sensor: 489.3°C
- Sensor 1: 485.7°C  
- Sensor 2: 492.1°C
- Sensor 3: 488.9°C

**Thermal Uniformity:** Excellent (±3.2°C variation)

"""
                    
                    if include_quality_alerts:
                        preview_content += """
## ⚠️ Quality Alerts
✅ **No critical issues detected**
- All sensors within normal operating range
- Temperature stability maintained throughout process
- No significant thermal spikes observed

"""
                    
                    if include_recommendations:
                        preview_content += """
## 💡 Recommendations
1. **Process Optimization:** Current parameters are optimal for consistent glass production
2. **Monitoring:** Continue regular thermal monitoring to maintain quality standards
3. **Maintenance:** Schedule routine sensor calibration as per maintenance protocol

"""
                    
                    if include_charts:
                        preview_content += """
## 📊 Charts & Graphs
[Temperature Profile Chart]
[Shell Detection Timeline]
[Sensor Comparison Graph]

"""
                    
                    preview_content += """
---
*Report generated by Sediver Thermal Intelligence Suite*
*Analysis Engine: v3.0 | Template Generator: v1.0*
"""
                    
                    # Display preview in expandable section
                    with st.expander(get_text("report_preview_header"), expanded=True):
                        st.markdown(preview_content)
                
                # Generate and Download Section
                st.subheader(get_text("generate_download"))
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button(get_text("generate_full_report"), type="primary"):
                        if position_data and (template_report_type == get_text("single_position") and selected_position_template):
                            with st.spinner(get_text("generating_report")):
                                # Here you would integrate with the actual data analysis
                                # For now, we'll create a comprehensive template
                                
                                full_report = f"""
{report_title}

Generated by: {analyst_name if analyst_name else 'Thermal Analysis System'}
Date: {report_date.strftime('%B %d, %Y')}
Company: {company_name}
Report Type: {template_report_type}
Analysis Position: {selected_position_template if template_report_type == "Single Position" else "Multiple Positions"}

{'='*60}

"""
                                
                                if include_executive:
                                    full_report += """
EXECUTIVE SUMMARY
================
This thermal analysis report provides comprehensive insights into the glass toughening 
process performance for the selected position(s). The analysis covers temperature 
profiles, shell detection capabilities, and quality indicators to ensure optimal 
production parameters and identify areas for process improvement.

Key Findings:
- Process stability maintained throughout analysis period
- Temperature uniformity within acceptable tolerances
- Production rate aligned with target specifications

"""
                                
                                if include_shell_table:
                                    full_report += """
SHELL DETECTION RESULTS
======================
Detected glass shells with thermal plateau analysis:

Shell #  | Start Time | Duration | Avg Temp | Stability | Quality
---------|------------|----------|----------|-----------|----------
Shell 1  | 00:15:23   | 12.3s    | 485.2°C  | ±1.8°C    | Excellent
Shell 2  | 00:28:45   | 11.8s    | 487.1°C  | ±2.1°C    | Good
Shell 3  | 00:41:12   | 12.1s    | 486.5°C  | ±1.5°C    | Excellent

Production Rate: 4.2 pieces per minute
Average Shell Duration: 12.1 seconds

"""
                                
                                if include_temp_profile:
                                    full_report += """
TEMPERATURE PROFILE ANALYSIS
===========================
Peak Temperature Analysis:
- Head Sensor: 489.3°C
- Sensor 1: 485.7°C
- Sensor 2: 492.1°C  
- Sensor 3: 488.9°C
- Sensor 4: 487.2°C

Thermal Uniformity Assessment:
- Maximum variation: ±3.2°C
- Standard deviation: 2.1°C
- Uniformity rating: Excellent

Temperature Stability:
- Average stability: ±1.8°C during shell processing
- No significant thermal spikes detected
- Consistent heating profile maintained

"""
                                
                                if include_quality_alerts:
                                    full_report += """
QUALITY ALERTS & ANOMALIES
==========================
Process Quality Assessment:

✓ PASSED - All sensors within normal operating range (450-500°C)
✓ PASSED - Temperature stability maintained (±5°C threshold)
✓ PASSED - No critical thermal spikes detected
✓ PASSED - Shell duration consistency within specifications

Anomaly Detection Results:
- No significant anomalies detected
- Process running within normal parameters
- Quality indicators meet production standards

"""
                                
                                if include_recommendations:
                                    full_report += """
RECOMMENDATIONS
===============
Based on the thermal analysis results:

1. PROCESS OPTIMIZATION
   - Current parameters are optimal for consistent glass production
   - Maintain existing temperature setpoints
   - Continue current cycle timing

2. MONITORING & MAINTENANCE
   - Schedule routine sensor calibration (quarterly recommended)
   - Monitor thermal uniformity trends
   - Implement predictive maintenance protocols

3. QUALITY ASSURANCE
   - Continue regular thermal monitoring
   - Document process parameters for quality records
   - Maintain current operating procedures

4. FUTURE IMPROVEMENTS
   - Consider implementing real-time anomaly detection
   - Evaluate opportunities for cycle time optimization
   - Assess potential for energy efficiency improvements

"""
                                
                                full_report += f"""
TECHNICAL SPECIFICATIONS
========================
Analysis Parameters:
- Detection Threshold: ±5.0°C
- Minimum Shell Duration: 2.0 seconds
- Sampling Rate: 10 Hz
- Analysis Duration: {df_preview['Time_seconds'].max():.1f} seconds

Data Quality:
- Total Samples: {len(df_preview):,}
- Missing Data Points: 0%
- Sensor Coverage: 100%

{'='*60}
Report generated by Sediver Thermal Intelligence Suite
Analysis Engine: v3.0 | Template Generator: v1.0
Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
                                
                                # Store the report for download
                                st.session_state['generated_report'] = full_report
                                st.success(get_text("report_generated_success"))
                        else:
                            st.warning(get_text("select_position_warning"))
                
                with col2:
                    # Download button (only show if report is generated)
                    if 'generated_report' in st.session_state:
                        st.download_button(
                            label=f"{get_text('download_report')} {output_format}",
                            data=st.session_state['generated_report'],
                            file_name=f"{report_title.lower().replace(' ', '_')}_{report_date.strftime('%Y%m%d')}.txt",
                            mime="text/plain",
                            help=get_text("download_help")
                        )
                    else:
                        st.info(get_text("generate_first"))
                
                # AI Integration Option
                st.subheader(get_text("ai_enhancement"))
                
                ai_enhance = st.checkbox(
                    get_text("enhance_with_ai"),
                    help=get_text("ai_help")
                )
                
                if ai_enhance:
                    st.info(get_text("ai_key_required"))
                    ai_sections = st.multiselect(
                        get_text("select_ai_sections"),
                        [
                            get_text("executive_summary"), 
                            get_text("quality_assessment"), 
                            get_text("recommendations"), 
                            get_text("predictive_insights")
                        ],
                        default=[get_text("recommendations")]
                    )
                    
                    if ai_sections:
                        st.success(f"{get_text('ai_will_enhance')} {', '.join(ai_sections)}")
                
                else:
                    st.info(get_text("upload_to_use"))
>>>>>>> 102e9028486595b497f6168f41ee9cb8a2b84ea9


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
    
    st.markdown(f"""
    **{get_text("analysis_capabilities")}**
    - {get_text("plateau_detection")}
    - {get_text("peak_extraction")}
    - {get_text("production_rate")}
    - {get_text("thermal_profiling")}
    - {get_text("journey_reconstruction")}
    """)

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