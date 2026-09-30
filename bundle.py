import os

base_dir = r"c:\Users\perei\OneDrive\Documentos\VSCODE\Checklist_EEAR"

with open(os.path.join(base_dir, "style.css"), "r", encoding="utf-8") as f:
    css = f.read()

with open(os.path.join(base_dir, "data.js"), "r", encoding="utf-8") as f:
    data_js = f.read()

with open(os.path.join(base_dir, "app.js"), "r", encoding="utf-8") as f:
    app_js = f.read()

# Original template
template = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EEAR CHECKLIST — Preparatório Oficial & Rastreador de Estudos</title>
  <meta name="description" content="Checklist completo e interativo de estudos para o concurso da EEAR com acompanhamento de progresso, simulados, caderno de erros e bizus da banca.">
  <meta property="og:title" content="EEAR CHECKLIST — Preparatório Oficial & Rastreador de Estudos">
  <meta property="og:description" content="Checklist oficial e interativo com edital verticalizado, simulador de questões, caderno de erros e bizus táticos da banca EEAR.">
  <meta property="og:type" content="website">
  <meta name="theme-color" content="#0b1120">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>✈️</text></svg>">
  <style>
{css}
  </style>
</head>
<body>

  <div class="app-container">
    
    <!-- Top Aeronautics Checklist Navbar -->
    <header class="top-navbar">
      <div class="brand-group">
        <div class="brand-badge">✈️</div>
        <div>
          <h1 class="brand-title">EEAR CHECKLIST</h1>
          <div class="brand-subtitle">
            <span class="status-indicator"></span>
            Progresso Salvo Automaticamente no seu Navegador
          </div>
        </div>
      </div>

      <div class="nav-actions">
        <button class="btn-pill" onclick="exportBackup()" title="Baixar arquivo de backup com todas as suas marcações">
          📥 Exportar Backup (.JSON)
        </button>
        <button class="btn-pill" onclick="document.getElementById('backupFileInput').click()" title="Restaurar backup anterior">
          📤 Importar Backup
        </button>
        <button class="btn-pill" onclick="resetAllData()" style="color: var(--accent-rose); border-color: rgba(244, 63, 94, 0.35);" title="Zerar todos os dados para recomeçar o checklist do zero">
          🔄 Zerar Dados
        </button>
        <input type="file" id="backupFileInput" style="display: none;" accept=".json" onchange="importBackup(event)">
      </div>
    </header>

    <!-- Universal Exam Countdown HUD Banner (CFS 2/2027) -->
    <section class="exam-countdown-banner">
      <div class="countdown-badge-group">
        <div class="countdown-live-dot"></div>
        <div class="countdown-label-group">
          <span class="countdown-title">OPERAÇÃO CFS 2/2027 • PROVA OBJETIVA (96 QUESTÕES)</span>
          <span class="countdown-subtitle">Contagem regressiva para o dia da prova • <strong>22 de Novembro de 2026</strong> (4h20min oficiais)</span>
        </div>
      </div>

      <div class="countdown-units-grid">
        <div class="countdown-unit">
          <span class="countdown-digit" id="countdownDays">00</span>
          <span class="countdown-unit-label">DIAS</span>
        </div>
        <span class="countdown-colon">:</span>
        <div class="countdown-unit">
          <span class="countdown-digit" id="countdownHours">00</span>
          <span class="countdown-unit-label">HORAS</span>
        </div>
        <span class="countdown-colon">:</span>
        <div class="countdown-unit">
          <span class="countdown-digit" id="countdownMins">00</span>
          <span class="countdown-unit-label">MIN</span>
        </div>
        <span class="countdown-colon">:</span>
        <div class="countdown-unit">
          <span class="countdown-digit" id="countdownSecs">00</span>
          <span class="countdown-unit-label">SEG</span>
        </div>
      </div>

      <div class="countdown-target-status">
        <span class="status-pill-official">🎯 EDITAL CFS 2/2027</span>
      </div>
    </section>

    <!-- Global Analytics Dashboard Bar -->
    <section class="hero-dashboard">
      <div class="metric-card highlight">
        <div class="metric-header">
          <span class="metric-title">Progresso Geral do Edital</span>
          <span class="metric-icon">🚀</span>
        </div>
        <div class="metric-value-group">
          <span class="metric-value" id="heroOverallProgress">0%</span>
          <span class="metric-subtext">do conteúdo programático dominado</span>
        </div>
        <div class="progress-track">
          <div class="progress-fill" id="heroProgressBar" style="width: 0%;"></div>
        </div>
      </div>

      <div class="metric-card">
        <div class="metric-header">
          <span class="metric-title">Tópicos Concluídos</span>
          <span class="metric-icon">✅</span>
        </div>
        <div class="metric-value-group">
          <span class="metric-value" id="heroCompletedCount">0 / 0</span>
        </div>
        <span class="metric-subtext">Teoria + Fixação realizadas</span>
      </div>

      <div class="metric-card">
        <div class="metric-header">
          <span class="metric-title">Provas Simuladas</span>
          <span class="metric-icon">🎯</span>
        </div>
        <div class="metric-value-group">
          <span class="metric-value" id="heroExamsDone">0</span>
          <span class="metric-subtext">de 20 provas oficiais</span>
        </div>
        <span class="metric-subtext">Treino com tempo cronometrado</span>
      </div>

      <div class="metric-card">
        <div class="metric-header">
          <span class="metric-title">Caderno de Erros</span>
          <span class="metric-icon">🧠</span>
        </div>
        <div class="metric-value-group">
          <span class="metric-value" id="heroErrorsCount" style="color: var(--accent-rose);">0</span>
          <span class="metric-subtext">questões registradas</span>
        </div>
        <span class="metric-subtext">Pontos cegos mapeados para revisão</span>
      </div>
    </section>

    <!-- Navigation Tabs & Real-time Search -->
    <div class="nav-tabs-wrapper">
      <div class="subject-tabs">
        <button class="tab-btn active" data-tab="dashboard" onclick="switchTab('dashboard')">
          📊 Visão Geral
        </button>
        <button class="tab-btn" data-tab="portugues" onclick="switchTab('portugues')">
          📖 Português <span class="badge-count" id="badge-portugues">0%</span>
        </button>
        <button class="tab-btn" data-tab="ingles" onclick="switchTab('ingles')">
          🇬🇧 Inglês <span class="badge-count" id="badge-ingles">0%</span>
        </button>
        <button class="tab-btn" data-tab="matematica" onclick="switchTab('matematica')">
          📐 Matemática <span class="badge-count" id="badge-matematica">0%</span>
        </button>
        <button class="tab-btn" data-tab="fisica" onclick="switchTab('fisica')">
          ⚡ Física <span class="badge-count" id="badge-fisica">0%</span>
        </button>
        <button class="tab-btn" data-tab="simulados" onclick="switchTab('simulados')">
          🎯 Simulados & Provas
        </button>
        <button class="tab-btn" data-tab="erros" onclick="switchTab('erros')">
          🧠 Caderno de Erros
        </button>
        <button class="tab-btn" data-tab="guia" onclick="switchTab('guia')">
          📚 Bibliografia & Guia
        </button>
      </div>

      <div class="search-filter-box">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" class="search-input" id="globalSearchInput" placeholder="Pesquisar por assunto, fórmula ou bizu...">
        </div>
      </div>
    </div>

    <!-- Main Dynamic Content Area -->
    <main id="mainContentArea">
      <!-- Injected dynamically via script -->
    </main>

  </div>

  <!-- Tactical Floating Study Cockpit / Timer Widget -->
  <div class="study-cockpit" id="studyCockpit" title="Estação Tática de Estudos EEAR">
    <!-- Main Floating Capsule / HUD Bar -->
    <div class="cockpit-bar" id="cockpitBar" onclick="toggleCockpitExpand(event)">
      <!-- Animated Circular Progress Ring with Mode Icon -->
      <div class="cockpit-ring-box">
        <svg class="cockpit-svg-ring" width="40" height="40" viewBox="0 0 40 40">
          <circle class="cockpit-ring-bg" cx="20" cy="20" r="16" fill="none" stroke-width="3"></circle>
          <circle class="cockpit-ring-fill" id="timerRingProgress" cx="20" cy="20" r="16" fill="none" stroke-width="3" stroke-dasharray="100.53" stroke-dashoffset="0"></circle>
        </svg>
        <span class="cockpit-center-icon" id="cockpitModeIcon">🍅</span>
      </div>

      <!-- Time and Mode Info -->
      <div class="cockpit-info">
        <div class="cockpit-mode-line">
          <span class="cockpit-mode-label" id="cockpitModeLabel">Pomodoro Foco</span>
          <span class="cockpit-live-pulse" id="cockpitLivePulse"></span>
        </div>
        <div class="cockpit-timer-digits" id="timerDisplay">25:00</div>
      </div>

      <!-- Quick Action Controls -->
      <div class="cockpit-controls" onclick="event.stopPropagation()">
        <button class="cockpit-btn primary" id="timerToggleBtn" onclick="toggleTimer()" title="Iniciar / Pausar">
          <span id="timerPlayIcon">▶</span>
        </button>
        <button class="cockpit-btn" onclick="resetTimer()" title="Reiniciar Tempo">↺</button>
        <button class="cockpit-btn options-btn" id="cockpitExpandToggleBtn" onclick="toggleCockpitExpand(event)" title="Abrir Modos & Variações">⚡</button>
      </div>
    </div>

    <!-- Expandable Tactical Drawer with 6 Study Presets & Tools -->
    <div class="cockpit-drawer" id="cockpitDrawer">
      <div class="cockpit-drawer-header">
        <div class="drawer-title-group">
          <span class="drawer-badge">EEAR TACTICAL</span>
          <span class="drawer-title">Modos de Estudo & Ritmo de Prova</span>
        </div>
        <div class="drawer-actions">
          <button class="cockpit-sound-pill active" id="soundToggleBtn" onclick="toggleTimerSound()" title="Ativar ou desativar aviso sonoro">
            <span id="soundIcon">🔊</span> <span id="soundText">Som: ON</span>
          </button>
          <button class="cockpit-close-pill" onclick="toggleCockpitExpand(event)" title="Recolher painel">✕</button>
        </div>
      </div>

      <div class="cockpit-presets-grid">
        <div class="preset-card active" id="preset-pomodoro" onclick="setTimerPreset('pomodoro')">
          <div class="preset-card-top">
            <span class="preset-icon">🍅</span>
            <span class="preset-pill">25 min</span>
          </div>
          <span class="preset-title">Pomodoro Clássico</span>
          <span class="preset-desc">Foco absoluto para teoria, resumos e videoaulas.</span>
        </div>

        <div class="preset-card" id="preset-sprint" onclick="setTimerPreset('sprint')">
          <div class="preset-card-top">
            <span class="preset-icon">⚡</span>
            <span class="preset-pill highlight">2m 40s</span>
          </div>
          <span class="preset-title">Sprint Questão EEAR</span>
          <span class="preset-desc">Tempo oficial por questão (96 questões em 4h20m).</span>
        </div>

        <div class="preset-card" id="preset-bloco50" onclick="setTimerPreset('bloco50')">
          <div class="preset-card-top">
            <span class="preset-icon">🎯</span>
            <span class="preset-pill">50 min</span>
          </div>
          <span class="preset-title">Bloco de Treino</span>
          <span class="preset-desc">Bateria de 15 a 25 exercícios de fixação sem distrações.</span>
        </div>

        <div class="preset-card" id="preset-simulado" onclick="setTimerPreset('simulado')">
          <div class="preset-card-top">
            <span class="preset-icon">✈️</span>
            <span class="preset-pill aero">4h 20m</span>
          </div>
          <span class="preset-title">Simulado Prova Real</span>
          <span class="preset-desc">260 minutos de combate para rodar uma prova oficial completa.</span>
        </div>

        <div class="preset-card" id="preset-pausa5" onclick="setTimerPreset('pausa5')">
          <div class="preset-card-top">
            <span class="preset-icon">☕</span>
            <span class="preset-pill">5 min</span>
          </div>
          <span class="preset-title">Pausa Tática</span>
          <span class="preset-desc">Levante, tome água, respire fundo e alongue.</span>
        </div>

        <div class="preset-card" id="preset-stopwatch" onclick="setTimerPreset('stopwatch')">
          <div class="preset-card-top">
            <span class="preset-icon">⏱️</span>
            <span class="preset-pill">Livre</span>
          </div>
          <span class="preset-title">Cronômetro Aberto</span>
          <span class="preset-desc">Contagem progressiva para medir tempo líquido do dia.</span>
        </div>
      </div>

      <div class="cockpit-drawer-footer">
        <div class="cockpit-streak-box">
          <span class="streak-icon">🔥</span>
          <span class="streak-text">Blocos de estudo dominados hoje: <strong id="todaySessionsDisplay">0</strong></span>
        </div>
        <span class="cockpit-hint">💡 Dica: Ao terminar, toca um suave aviso de cabine aeronáutica!</span>
      </div>
    </div>
  </div>

  <!-- Notification Toast -->
  <div class="toast-msg" id="toastMsg">✓ Progresso salvo automaticamente!</div>

  <!-- Embedded Core Data & Application Logic -->
  <script>
{data_js}
  </script>
  <script>
{app_js}
  </script>
</body>
</html>
"""

# Save to index.html (self-contained) and EEAR_CHECKLIST_PORTATIL.html
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(template)

with open(os.path.join(base_dir, "EEAR_CHECKLIST_PORTATIL.html"), "w", encoding="utf-8") as f:
    f.write(template)

print("Both index.html and EEAR_CHECKLIST_PORTATIL.html generated successfully!")
