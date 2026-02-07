from flask import Flask, Response

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Yunix Arcade OS – Locked Desktop</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    *{margin:0;padding:0;box-sizing:border-box;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;}
    :root{
      --bg-main:#020617;
      --bg-window:#020617;
      --border-soft:rgba(148,163,184,0.5);
      --accent:#38bdf8;
      --accent-soft:rgba(56,189,248,0.18);
      --text-main:#e5e7eb;
      --text-soft:#9ca3af;
      --radius-lg:22px;
      --radius-md:18px;
      --radius-sm:10px;
    }
    body{
      background:#020617;
      color:var(--text-main);
      min-height:100vh;
      display:flex;
      align-items:center;
      justify-content:center;
      overflow:hidden;
    }

    /* BACKGROUND */
    .bg-orb{
      position:fixed;
      border-radius:999px;
      filter:blur(40px);
      opacity:0.55;
      mix-blend-mode:screen;
      pointer-events:none;
      animation:float 18s ease-in-out infinite alternate;
    }
    .bg-orb.one{
      width:360px;height:360px;
      background:radial-gradient(circle,#38bdf8,#1d4ed8);
      top:-80px;left:-40px;
    }
    .bg-orb.two{
      width:320px;height:320px;
      background:radial-gradient(circle,#22c55e,#15803d);
      bottom:-80px;right:-40px;
      animation-delay:3s;
    }
    .bg-orb.three{
      width:260px;height:260px;
      background:radial-gradient(circle,#f97316,#c026d3);
      top:40%;left:60%;
      animation-delay:6s;
    }
    .bg-grid{
      position:fixed;
      inset:0;
      background-image:linear-gradient(rgba(148,163,184,0.08) 1px,transparent 1px),
                       linear-gradient(90deg,rgba(148,163,184,0.08) 1px,transparent 1px);
      background-size:40px 40px;
      opacity:0.25;
      pointer-events:none;
    }
    @keyframes float{
      0%{transform:translate3d(0,0,0) scale(1);}
      100%{transform:translate3d(40px,-30px,0) scale(1.1);}
    }

    .yunix-shell{
      position:relative;
      width:100%;
      height:100vh;
      max-width:1400px;
      max-height:820px;
      margin:auto;
      border-radius:var(--radius-lg);
      border:1px solid rgba(148,163,184,0.6);
      background:radial-gradient(circle at top,#020617,#020617 40%,#020617 100%);
      overflow:hidden;
      box-shadow:0 26px 80px rgba(0,0,0,0.9);
      backdrop-filter:blur(26px);
      display:flex;
      flex-direction:column;
    }

    /* TOP BAR */
    .top-status{
      height:40px;
      padding:0 16px;
      display:flex;
      align-items:center;
      justify-content:space-between;
      font-size:11px;
      color:var(--text-soft);
      background:linear-gradient(90deg,rgba(15,23,42,0.96),rgba(15,23,42,0.7));
      border-bottom:1px solid rgba(51,65,85,0.9);
    }
    .top-left{
      display:flex;
      align-items:center;
      gap:10px;
    }
    .logo-mark{
      width:18px;height:18px;border-radius:6px;
      background:conic-gradient(from 180deg,var(--accent),#22c55e,#f97316,#6366f1,var(--accent));
      display:flex;
      align-items:center;
      justify-content:center;
      box-shadow:0 0 18px rgba(56,189,248,0.6);
    }
    .logo-mark-inner{
      width:12px;height:12px;border-radius:4px;
      background:#020617;
    }
    .logo-text{
      font-weight:800;
      letter-spacing:0.18em;
      text-transform:uppercase;
      font-size:13px;
    }
    .logo-text span{color:var(--accent);}
    .top-pill{
      padding:4px 10px;
      border-radius:999px;
      border:1px solid rgba(75,85,99,0.9);
      background:rgba(15,23,42,0.9);
      display:flex;
      align-items:center;
      gap:6px;
    }
    .top-pill span{
      width:7px;height:7px;border-radius:999px;
      background:#22c55e;
      box-shadow:0 0 10px #22c55e;
    }
    .top-right{
      display:flex;
      align-items:center;
      gap:10px;
    }

    /* LOCK SCREEN (ANTES DO LOGIN) */
    .lock-screen{
      position:absolute;
      inset:0;
      display:flex;
      flex-direction:column;
      align-items:center;
      justify-content:center;
      background:radial-gradient(circle at top,#020617,#020617 60%,#020617 100%);
      z-index:50;
      animation:fadeIn 0.3s ease-out;
    }
    .lock-card{
      width:360px;
      max-width:92%;
      border-radius:var(--radius-md);
      border:1px solid rgba(148,163,184,0.7);
      background:rgba(15,23,42,0.96);
      box-shadow:0 24px 70px rgba(0,0,0,0.95);
      padding:16px 18px 14px;
      text-align:left;
    }
    .lock-title{
      font-size:16px;
      font-weight:600;
      margin-bottom:4px;
    }
    .lock-sub{
      font-size:12px;
      color:var(--text-soft);
      margin-bottom:10px;
    }
    .tab-row{
      display:flex;
      gap:6px;
      margin-bottom:10px;
    }
    .tab-btn{
      flex:1;
      text-align:center;
      padding:6px 0;
      border-radius:999px;
      border:1px solid rgba(55,65,81,0.9);
      background:rgba(15,23,42,0.9);
      cursor:pointer;
      font-size:11px;
      color:var(--text-soft);
    }
    .tab-btn.active{
      background:linear-gradient(135deg,var(--accent),#6366f1);
      color:#0b1120;
      border-color:transparent;
      box-shadow:0 10px 26px rgba(56,189,248,0.45);
      font-weight:600;
    }
    .field{
      display:flex;
      flex-direction:column;
      gap:3px;
      margin-bottom:8px;
    }
    .field label{
      font-size:11px;
      color:var(--text-main);
    }
    .field input{
      border-radius:999px;
      border:1px solid rgba(55,65,81,0.9);
      background:rgba(15,23,42,0.96);
      padding:6px 10px;
      color:var(--text-main);
      font-size:11px;
      outline:none;
    }
    .field input:focus{
      border-color:var(--accent);
      box-shadow:0 0 0 1px rgba(56,189,248,0.5);
    }
    .btn{
      border:none;
      outline:none;
      cursor:pointer;
      border-radius:999px;
      padding:6px 12px;
      font-size:11px;
      display:inline-flex;
      align-items:center;
      gap:6px;
      transition:0.16s transform,0.16s box-shadow,0.16s background,0.16s opacity;
      white-space:nowrap;
    }
    .btn-primary{
      background:linear-gradient(135deg,var(--accent),#6366f1);
      color:#0b1120;
      box-shadow:0 12px 26px rgba(56,189,248,0.45);
      font-weight:600;
    }
    .btn-primary:hover{
      transform:translateY(-1px);
      box-shadow:0 16px 32px rgba(56,189,248,0.6);
    }
    .lock-hint{
      font-size:11px;
      color:var(--text-soft);
      margin-top:6px;
    }

    @keyframes fadeIn{
      from{opacity:0;transform:translateY(10px);}
      to{opacity:1;transform:translateY(0);}
    }

    /* DESKTOP (APÓS LOGIN) */
    .yunix-desktop{
      flex:1;
      position:relative;
      padding:16px 18px 0;
      display:flex;
      flex-direction:column;
      gap:12px;
      opacity:0;
      pointer-events:none;
      transition:0.25s opacity;
    }
    .yunix-desktop.active{
      opacity:1;
      pointer-events:auto;
    }
    .desktop-header{
      display:flex;
      justify-content:space-between;
      align-items:flex-end;
      gap:10px;
    }
    .desktop-title{
      font-size:18px;
      font-weight:600;
    }
    .desktop-sub{
      font-size:12px;
      color:var(--text-soft);
    }
    .desktop-quick{
      display:flex;
      align-items:center;
      gap:8px;
      font-size:11px;
      color:var(--text-soft);
    }
    .quick-dot{
      width:7px;height:7px;border-radius:999px;
      background:var(--accent);
    }

    .desktop-grid{
      flex:1;
      display:grid;
      grid-template-columns:2.2fr 1.4fr;
      gap:14px;
      padding:6px 0 10px;
    }
    .grid-left{
      display:grid;
      grid-template-columns:repeat(2,minmax(0,1fr));
      gap:12px;
    }
    .grid-right{
      display:flex;
      flex-direction:column;
      gap:12px;
    }

    .desktop-card{
      border-radius:var(--radius-md);
      border:1px solid rgba(51,65,85,0.9);
      background:linear-gradient(135deg,rgba(15,23,42,0.96),rgba(15,23,42,0.9));
      padding:12px;
      display:flex;
      flex-direction:column;
      gap:6px;
      position:relative;
      overflow:hidden;
    }
    .desktop-card::before{
      content:"";
      position:absolute;
      inset:0;
      background:radial-gradient(circle at top right,var(--accent-soft),transparent 60%);
      opacity:0;
      transition:0.2s opacity;
      pointer-events:none;
    }
    .desktop-card:hover::before{opacity:1;}
    .card-label{
      font-size:10px;
      color:var(--text-soft);
      text-transform:uppercase;
      letter-spacing:0.14em;
    }
    .card-title{
      font-size:14px;
      font-weight:600;
    }
    .card-sub{
      font-size:11px;
      color:var(--text-soft);
    }
    .card-actions{
      margin-top:auto;
      display:flex;
      gap:8px;
      flex-wrap:wrap;
    }
    .btn-ghost{
      background:rgba(15,23,42,0.9);
      color:var(--text-main);
      border:1px solid rgba(75,85,99,0.9);
    }
    .btn-ghost:hover{
      background:rgba(31,41,55,0.95);
      transform:translateY(-1px);
    }

    .activity-card{
      border-radius:var(--radius-md);
      border:1px solid rgba(51,65,85,0.9);
      background:rgba(15,23,42,0.9);
      padding:10px;
      display:flex;
      flex-direction:column;
      gap:6px;
      font-size:11px;
    }
    .activity-header{
      display:flex;
      justify-content:space-between;
      align-items:center;
    }
    .activity-list{
      margin-top:4px;
      display:flex;
      flex-direction:column;
      gap:4px;
      max-height:140px;
      overflow:auto;
      font-family:monospace;
      font-size:11px;
      color:var(--text-soft);
    }

    .widget-card{
      border-radius:var(--radius-md);
      border:1px solid rgba(51,65,85,0.9);
      background:rgba(15,23,42,0.9);
      padding:10px;
      display:flex;
      flex-direction:column;
      gap:6px;
      font-size:11px;
    }
    .widget-row{
      display:flex;
      justify-content:space-between;
      align-items:center;
      gap:8px;
    }
    .widget-label{color:var(--text-soft);}
    .widget-value{font-weight:600;}

    /* WINDOWS */
    .window{
      position:absolute;
      top:50%;
      left:50%;
      transform:translate(-50%,-50%);
      width:480px;
      max-width:92%;
      max-height:72%;
      border-radius:var(--radius-md);
      border:1px solid var(--border-soft);
      background:rgba(15,23,42,0.96);
      box-shadow:0 24px 70px rgba(0,0,0,0.95);
      overflow:hidden;
      display:none;
      flex-direction:column;
      z-index:10;
      animation:pop 0.18s ease-out;
      backdrop-filter:blur(20px);
    }
    .window-header{
      padding:8px 10px;
      display:flex;
      align-items:center;
      justify-content:space-between;
      background:linear-gradient(90deg,rgba(15,23,42,1),rgba(30,64,175,0.9));
      font-size:11px;
      color:var(--text-main);
    }
    .window-left{
      display:flex;
      align-items:center;
      gap:6px;
    }
    .window-dots{
      display:flex;
      gap:5px;
      align-items:center;
    }
    .dot{
      width:9px;height:9px;border-radius:999px;
    }
    .dot.red{background:#f97373;}
    .dot.yellow{background:#facc15;}
    .dot.green{background:#4ade80;}
    .window-title{
      font-weight:600;
    }
    .window-close{
      cursor:pointer;
      font-size:13px;
      padding:2px 6px;
      border-radius:6px;
      background:rgba(15,23,42,0.7);
      border:1px solid rgba(30,64,175,0.8);
    }
    .window-close:hover{
      background:rgba(248,113,113,0.15);
      border-color:#f97373;
      color:#fecaca;
    }
    .window-body{
      padding:10px 12px 12px;
      font-size:11px;
      color:var(--text-main);
      max-height:100%;
      overflow:auto;
    }
    .window-sub{
      font-size:11px;
      color:var(--text-soft);
      margin-bottom:8px;
    }

    /* ARCADE APP */
    .games-grid{
      display:grid;
      grid-template-columns:repeat(3,minmax(0,1fr));
      gap:8px;
      margin-top:8px;
    }
    .game-card{
      border-radius:12px;
      border:1px solid rgba(55,65,81,0.9);
      background:radial-gradient(circle at top,rgba(56,189,248,0.18),rgba(15,23,42,0.96));
      padding:8px;
      font-size:11px;
      cursor:pointer;
      display:flex;
      flex-direction:column;
      gap:4px;
      transition:0.16s transform,0.16s box-shadow,0.16s border-color;
    }
    .game-card:hover{
      transform:translateY(-2px);
      box-shadow:0 14px 30px rgba(15,23,42,0.9);
      border-color:var(--accent);
    }
    .game-title{font-weight:600;}
    .game-meta{color:var(--text-soft);font-size:10px;}

    /* PROFILE APP */
    .profile-row{
      font-size:12px;
      margin-bottom:4px;
    }

    /* ADMIN PANEL (FAKE) */
    .admin-grid{
      display:flex;
      flex-direction:column;
      gap:8px;
      margin-top:6px;
    }
    .admin-row{
      display:flex;
      justify-content:space-between;
      align-items:center;
      gap:8px;
      padding:7px 8px;
      border-radius:10px;
      border:1px solid rgba(55,65,81,0.9);
      background:rgba(15,23,42,0.96);
      font-size:11px;
    }

    /* GLOBAL CHAT (FAKE LOCAL) */
    .chat-box{
      border-radius:10px;
      border:1px solid rgba(55,65,81,0.9);
      background:rgba(15,23,42,0.96);
      padding:6px;
      max-height:180px;
      overflow:auto;
      font-size:11px;
    }
    .chat-msg{
      margin-bottom:4px;
    }
    .chat-meta{
      color:var(--text-soft);
      font-size:10px;
    }
    .chat-input-row{
      display:flex;
      gap:6px;
      margin-top:6px;
    }
    .chat-input-row input{
      flex:1;
      border-radius:999px;
      border:1px solid rgba(55,65,81,0.9);
      background:rgba(15,23,42,0.96);
      padding:6px 10px;
      color:var(--text-main);
      font-size:11px;
      outline:none;
    }

    /* SETTINGS APP */
    .settings-list{
      display:flex;
      flex-direction:column;
      gap:8px;
      margin-top:6px;
    }
    .setting-row{
      display:flex;
      justify-content:space-between;
      align-items:center;
      gap:8px;
      padding:7px 8px;
      border-radius:10px;
      border:1px solid rgba(55,65,81,0.9);
      background:rgba(15,23,42,0.96);
      font-size:11px;
    }
    .setting-label{color:var(--text-main);}
    .setting-desc{color:var(--text-soft);font-size:10px;}
    .toggle{
      width:34px;height:18px;
      border-radius:999px;
      background:rgba(31,41,55,1);
      border:1px solid rgba(75,85,99,1);
      position:relative;
      cursor:pointer;
      transition:0.16s background,0.16s border-color;
    }
    .toggle::after{
      content:"";
      position:absolute;
      top:2px;left:2px;
      width:12px;height:12px;
      border-radius:999px;
      background:#9ca3af;
      transition:0.16s;
    }
    .toggle.on{
      background:rgba(22,163,74,0.3);
      border-color:#22c55e;
    }
    .toggle.on::after{
      transform:translateX(14px);
      background:#bbf7d0;
    }

    /* TASKBAR + START MENU */
    .taskbar{
      height:42px;
      border-top:1px solid rgba(51,65,85,0.9);
      background:rgba(15,23,42,0.96);
      display:flex;
      align-items:center;
      justify-content:space-between;
      padding:0 10px;
      font-size:11px;
      color:var(--text-soft);
      backdrop-filter:blur(18px);
    }
    .task-left{
      display:flex;
      align-items:center;
      gap:8px;
    }
    .start-btn{
      border-radius:999px;
      border:1px solid rgba(75,85,99,0.9);
      background:rgba(15,23,42,0.96);
      padding:4px 10px;
      display:flex;
      align-items:center;
      gap:6px;
      cursor:pointer;
      color:var(--text-main);
    }
    .start-icon{
      width:12px;height:12px;border-radius:3px;
      background:linear-gradient(135deg,var(--accent),#22c55e);
    }
    .task-apps{
      display:flex;
      gap:4px;
      align-items:center;
    }
    .task-pill{
      padding:3px 8px;
      border-radius:999px;
      background:rgba(15,23,42,0.9);
      border:1px solid rgba(55,65,81,0.9);
      color:var(--text-main);
      cursor:pointer;
    }
    .task-right{
      display:flex;
      align-items:center;
      gap:10px;
    }

    .start-menu{
      position:absolute;
      left:10px;
      bottom:46px;
      width:280px;
      border-radius:var(--radius-md);
      border:1px solid rgba(148,163,184,0.7);
      background:rgba(15,23,42,0.98);
      box-shadow:0 20px 60px rgba(0,0,0,0.9);
      padding:10px;
      font-size:11px;
      display:none;
      flex-direction:column;
      gap:8px;
      z-index:20;
      backdrop-filter:blur(18px);
    }
    .start-title{
      font-size:12px;
      font-weight:600;
    }
    .start-grid{
      display:grid;
      grid-template-columns:repeat(3,minmax(0,1fr));
      gap:6px;
      margin-top:4px;
    }
    .start-app{
      border-radius:10px;
      border:1px solid rgba(55,65,81,0.9);
      background:rgba(15,23,42,0.96);
      padding:6px;
      text-align:center;
      cursor:pointer;
    }
    .start-app span{
      display:block;
      font-size:10px;
      margin-top:4px;
      color:var(--text-soft);
    }

    @keyframes pop{
      from{transform:translate(-50%,-50%) scale(0.9);opacity:0;}
      to{transform:translate(-50%,-50%) scale(1);opacity:1;}
    }

    @media(max-width:900px){
      .yunix-shell{
        border-radius:0;
        max-width:none;
        max-height:none;
      }
      .desktop-grid{
        grid-template-columns:1fr;
      }
      .grid-left{
        grid-template-columns:1fr;
      }
      .window{
        width:92%;
      }
    }
  </style>
</head>
<body>
  <div class="bg-orb one"></div>
  <div class="bg-orb two"></div>
  <div class="bg-orb three"></div>
  <div class="bg-grid"></div>

  <div class="yunix-shell">
    <div class="top-status">
      <div class="top-left">
        <div class="logo-mark"><div class="logo-mark-inner"></div></div>
        <div class="logo-text">YUNIX<span>OS</span></div>
        <div class="top-pill"><span></span> ARCADE PLATFORM • LOCKED DESKTOP</div>
      </div>
      <div class="top-right">
        <div id="top-clock">--:--</div>
      </div>
    </div>

    <!-- LOCK SCREEN -->
    <div class="lock-screen" id="lock-screen">
      <div class="lock-card">
        <div class="lock-title">Welcome to Yunix Arcade OS</div>
        <div class="lock-sub">
          Sign in or create an account to unlock the desktop and access apps, arcade, admin panel and global chat.
        </div>

        <div class="tab-row">
          <div class="tab-btn active" id="lock-tab-login" onclick="switchLockTab('login')">LOGIN</div>
          <div class="tab-btn" id="lock-tab-signup" onclick="switchLockTab('signup')">CREATE ACCOUNT</div>
        </div>

        <div id="lock-login">
          <div class="field">
            <label>Username</label>
            <input id="lock-login-username" placeholder="Enter username" />
          </div>
          <div class="field">
            <label>Password</label>
            <input id="lock-login-password" type="password" placeholder="Enter password" />
          </div>
          <button class="btn btn-primary" onclick="lockLogin()">Sign in</button>
        </div>

        <div id="lock-signup" style="display:none;">
          <div class="field">
            <label>Username</label>
            <input id="lock-signup-username" placeholder="Choose a username" />
          </div>
          <div class="field">
            <label>Email</label>
            <input id="lock-signup-email" placeholder="Enter email" />
          </div>
          <div class="field">
            <label>Password</label>
            <input id="lock-signup-password" type="password" placeholder="Create password" />
          </div>
          <button class="btn btn-primary" onclick="lockSignup()">Create account</button>
        </div>

        <div class="lock-hint">
          All data is local and resets on refresh. This is a front‑end only demo, perfect for showing the UX.
        </div>
      </div>
    </div>

    <!-- DESKTOP -->
    <div class="yunix-desktop" id="desktop">
      <div class="desktop-header">
        <div>
          <div class="desktop-title">Yunix Arcade Desktop</div>
          <div class="desktop-sub">
            Desktop‑style shell with apps, arcade, admin panel and global chat. Unlocked after login.
          </div>
        </div>
        <div class="desktop-quick">
          <div class="quick-dot"></div>
          <div id="quick-status">Desktop locked. Use the login screen to get access.</div>
        </div>
      </div>

      <div class="desktop-grid">
        <div class="grid-left">
          <div class="desktop-card">
            <div class="card-label">Arcade</div>
            <div class="card-title">Game Hub</div>
            <div class="card-sub">
              Browse featured games, launch them and gain XP in your local profile.
            </div>
            <div class="card-actions">
              <button class="btn btn-primary" onclick="openWindow('arcade')">Open Arcade</button>
            </div>
          </div>

          <div class="desktop-card">
            <div class="card-label">Admin</div>
            <div class="card-title">Admin Panel (fake)</div>
            <div class="card-sub">
              Simulated admin controls: user count, sessions, flags. Great for demoing a control center.
            </div>
            <div class="card-actions">
              <button class="btn btn-primary" onclick="openWindow('admin')">Open Admin Panel</button>
            </div>
          </div>

          <div class="desktop-card">
            <div class="card-label">Social</div>
            <div class="card-title">Global Chat (local)</div>
            <div class="card-sub">
              Fake “global” chat. Messages stay only in this browser tab, but feel like a shared channel.
            </div>
            <div class="card-actions">
              <button class="btn btn-primary" onclick="openWindow('chat')">Open Chat</button>
            </div>
          </div>

          <div class="desktop-card">
            <div class="card-label">Profile</div>
            <div class="card-title">Progress & Level</div>
            <div class="card-sub">
              Local level and XP bar. Launch games to level up and show off your fake grind.
            </div>
            <div class="card-actions">
              <button class="btn btn-primary" onclick="openWindow('profile')">Open Profile</button>
            </div>
          </div>
        </div>

        <div class="grid-right">
          <div class="activity-card">
            <div class="activity-header">
              <div>Activity log</div>
              <div style="font-size:10px;color:var(--text-soft);">Local only • Not persisted</div>
            </div>
            <div class="activity-list" id="activity-log"></div>
          </div>

          <div class="widget-card">
            <div class="widget-row">
              <div class="widget-label">Active windows</div>
              <div class="widget-value" id="widget-windows">0</div>
            </div>
            <div class="widget-row">
              <div class="widget-label">Last app</div>
              <div class="widget-value" id="widget-last">None</div>
            </div>
            <div class="widget-row">
              <div class="widget-label">Shell mode</div>
              <div class="widget-value" id="widget-mode">Dark • Blue accent</div>
            </div>
          </div>
        </div>
      </div>

      <!-- WINDOWS -->

      <!-- ARCADE WINDOW -->
      <div class="window" id="win-arcade">
        <div class="window-header">
          <div class="window-left">
            <div class="window-dots">
              <div class="dot red"></div>
              <div class="dot yellow"></div>
              <div class="dot green"></div>
            </div>
            <div class="window-title">Yunix Arcade – Game Hub</div>
          </div>
          <div class="window-close" onclick="closeWindow('arcade')">✕</div>
        </div>
        <div class="window-body">
          <div class="window-sub">
            Featured games. Click any card to “launch” it – this logs activity and gives XP to your profile.
          </div>
          <div class="games-grid">
            <div class="game-card" onclick="launchGame('Cyber Drift', 'Racing')">
              <div class="game-title">Cyber Drift</div>
              <div class="game-meta">Racing • 1.2k players</div>
            </div>
            <div class="game-card" onclick="launchGame('Neon Tactics', 'Strategy')">
              <div class="game-title">Neon Tactics</div>
              <div class="game-meta">Strategy • 860 players</div>
            </div>
            <div class="game-card" onclick="launchGame('Void Runner', 'Shooter')">
              <div class="game-title">Void Runner</div>
              <div class="game-meta">Shooter • 2.4k players</div>
            </div>
            <div class="game-card" onclick="launchGame('Pixel Arena', 'Arcade')">
              <div class="game-title">Pixel Arena</div>
              <div class="game-meta">Arcade • 540 players</div>
            </div>
            <div class="game-card" onclick="launchGame('Night City Rush', 'Action')">
              <div class="game-title">Night City Rush</div>
              <div class="game-meta">Action • 1.8k players</div>
            </div>
            <div class="game-card" onclick="launchGame('Quantum Lines', 'Puzzle')">
              <div class="game-title">Quantum Lines</div>
              <div class="game-meta">Puzzle • 320 players</div>
            </div>
          </div>
        </div>
      </div>

      <!-- ADMIN WINDOW -->
      <div class="window" id="win-admin">
        <div class="window-header">
          <div class="window-left">
            <div class="window-dots">
              <div class="dot red"></div>
              <div class="dot yellow"></div>
              <div class="dot green"></div>
            </div>
            <div class="window-title">Yunix Admin Panel (fake)</div>
          </div>
          <div class="window-close" onclick="closeWindow('admin')">✕</div>
        </div>
        <div class="window-body">
          <div class="window-sub">
            Simulated admin dashboard. Numbers are local and only for show, but the UI feels like a real control panel.
          </div>
          <div class="admin-grid">
            <div class="admin-row">
              <div>Registered users (local)</div>
              <div id="admin-users">1</div>
            </div>
            <div class="admin-row">
              <div>Active session</div>
              <div id="admin-session">Locked</div>
            </div>
            <div class="admin-row">
              <div>Games launched this session</div>
              <div id="admin-games">0</div>
            </div>
            <div class="admin-row">
              <div>Chat messages (local)</div>
              <div id="admin-chat">0</div>
            </div>
          </div>
        </div>
      </div>

      <!-- CHAT WINDOW -->
      <div class="window" id="win-chat">
        <div class="window-header">
          <div class="window-left">
            <div class="window-dots">
              <div class="dot red"></div>
              <div class="dot yellow"></div>
              <div class="dot green"></div>
            </div>
            <div class="window-title">Yunix Global Chat (local)</div>
          </div>
          <div class="window-close" onclick="closeWindow('chat')">✕</div>
        </div>
        <div class="window-body">
          <div class="window-sub">
            Messages stay only in this browser tab. Feels like a global chat, but it’s all local.
          </div>
          <div class="chat-box" id="chat-box"></div>
          <div class="chat-input-row">
            <input id="chat-input" placeholder="Type a message..." onkeydown="if(event.key==='Enter'){sendChat();}" />
            <button class="btn btn-primary" onclick="sendChat()">Send</button>
          </div>
        </div>
      </div>

      <!-- PROFILE WINDOW -->
      <div class="window" id="win-profile">
        <div class="window-header">
          <div class="window-left">
            <div class="window-dots">
              <div class="dot red"></div>
              <div class="dot yellow"></div>
              <div class="dot green"></div>
            </div>
            <div class="window-title">Yunix Arcade – Profile</div>
          </div>
          <div class="window-close" onclick="closeWindow('profile')">✕</div>
        </div>
        <div class="window-body">
          <div class="window-sub">
            Local profile only. Level and XP increase when you “launch” games from the Arcade window.
          </div>
          <div class="profile-row">
            Username: <span id="profile-username">Guest</span>
          </div>
          <div class="profile-row">
            Level: <span id="profile-level">1</span>
          </div>
          <div class="profile-row" style="font-size:11px;color:var(--text-soft);">
            XP: <span id="profile-xp">0</span> / <span id="profile-xp-max">100</span>
          </div>
          <div style="height:8px;border-radius:999px;border:1px solid rgba(55,65,81,0.9);overflow:hidden;margin-bottom:8px;">
            <div id="profile-xp-bar" style="height:100%;width:0%;background:linear-gradient(90deg,var(--accent),#22c55e);"></div>
          </div>
          <div style="font-size:11px;color:var(--text-soft);">
            Max level is basically infinite (we cap at a ridiculous number just for fun).
          </div>
        </div>
      </div>

      <!-- SETTINGS WINDOW -->
      <div class="window" id="win-settings">
        <div class="window-header">
          <div class="window-left">
            <div class="window-dots">
              <div class="dot red"></div>
              <div class="dot yellow"></div>
              <div class="dot green"></div>
            </div>
            <div class="window-title">Yunix Settings</div>
          </div>
          <div class="window-close" onclick="closeWindow('settings')">✕</div>
        </div>
        <div class="window-body">
          <div class="window-sub">
            Visual tweaks only. Everything is client‑side and resets when you refresh.
          </div>
          <div class="settings-list">
            <div class="setting-row">
              <div>
                <div class="setting-label">Light mode</div>
                <div class="setting-desc">Switch to a brighter shell.</div>
              </div>
              <div class="toggle" id="toggle-light" onclick="toggleLight()"></div>
            </div>
            <div class="setting-row">
              <div>
                <div class="setting-label">Green accent</div>
                <div class="setting-desc">Swap the main accent color.</div>
              </div>
              <div class="toggle" id="toggle-green" onclick="toggleGreen()"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- START MENU -->
    <div class="start-menu" id="start-menu">
      <div class="start-title">Yunix menu</div>
      <div class="window-sub">Quick access to core apps.</div>
      <div class="start-grid">
        <div class="start-app" onclick="openFromStart('arcade')">
          🎮<span>Arcade</span>
        </div>
        <div class="start-app" onclick="openFromStart('admin')">
          🛠️<span>Admin</span>
        </div>
        <div class="start-app" onclick="openFromStart('chat')">
          💬<span>Chat</span>
        </div>
        <div class="start-app" onclick="openFromStart('profile')">
          🧑<span>Profile</span>
        </div>
        <div class="start-app" onclick="openFromStart('settings')">
          ⚙️<span>Settings</span>
        </div>
      </div>
    </div>

    <!-- TASKBAR -->
    <div class="taskbar">
      <div class="task-left">
        <div class="start-btn" onclick="toggleStart()">
          <div class="start-icon"></div>
          <div>Yunix</div>
        </div>
        <div class="task-apps" id="task-apps"></div>
      </div>
      <div class="task-right">
        <div id="task-user">Locked</div>
        <div id="task-clock">--:--</div>
      </div>
    </div>
  </div>

  <script>
    // CLOCK
    function updateClock(){
      const now = new Date();
      const h = String(now.getHours()).padStart(2,"0");
      const m = String(now.getMinutes()).padStart(2,"0");
      const t = h + ":" + m;
      document.getElementById("top-clock").textContent = t;
      document.getElementById("task-clock").textContent = t;
    }
    setInterval(updateClock,1000);
    updateClock();

    // ACTIVITY LOG
    function log(msg){
      const box = document.getElementById("activity-log");
      const now = new Date();
      const t = now.toLocaleTimeString();
      box.textContent = "[" + t + "] " + msg + "\\n" + box.textContent;
    }

    // LOCK SCREEN LOGIC
    let registeredUsers = 0;
    let currentUser = null;

    function switchLockTab(tab){
      const loginTab = document.getElementById("lock-tab-login");
      const signupTab = document.getElementById("lock-tab-signup");
      const loginBox = document.getElementById("lock-login");
      const signupBox = document.getElementById("lock-signup");
      if(tab==="login"){
        loginTab.classList.add("active");
        signupTab.classList.remove("active");
        loginBox.style.display = "block";
        signupBox.style.display = "none";
      }else{
        signupTab.classList.add("active");
        loginTab.classList.remove("active");
        signupBox.style.display = "block";
        loginBox.style.display = "none";
      }
    }

    function unlockDesktop(username){
      currentUser = username || "Player";
      document.getElementById("lock-screen").style.display = "none";
      const desktop = document.getElementById("desktop");
      desktop.classList.add("active");
      document.getElementById("task-user").textContent = currentUser;
      document.getElementById("profile-username").textContent = currentUser;
      document.getElementById("quick-status").textContent = "Desktop unlocked. Use the start menu or cards to open apps.";
      document.getElementById("admin-session").textContent = "Active";
      log("Desktop unlocked for user: " + currentUser + " (local only).");
    }

    function lockLogin(){
      const user = document.getElementById("lock-login-username").value || "Player";
      unlockDesktop(user);
    }

    function lockSignup(){
      const user = document.getElementById("lock-signup-username").value || "NewPlayer";
      registeredUsers += 1;
      document.getElementById("admin-users").textContent = registeredUsers;
      unlockDesktop(user);
    }

    // WINDOWS + TASKBAR
    const openWindows = new Set();
    let gamesLaunched = 0;
    let chatMessages = 0;

    function openWindow(which){
      if(!currentUser){
        alert("You must log in first.");
        return;
      }
      const id = "win-" + which;
      const el = document.getElementById(id);
      if(!el) return;
      el.style.display = "flex";
      bringToFront(el);
      openWindows.add(which);
      renderTaskbar();
      closeStart();
      document.getElementById("quick-status").textContent = "Active app: " + prettyName(which);
      document.getElementById("widget-last").textContent = prettyName(which);
      document.getElementById("widget-windows").textContent = openWindows.size;
      log("Opened window: " + which);
    }
    function closeWindow(which){
      const id = "win-" + which;
      const el = document.getElementById(id);
      if(!el) return;
      el.style.display = "none";
      openWindows.delete(which);
      renderTaskbar();
      document.getElementById("widget-windows").textContent = openWindows.size;
      if(openWindows.size === 0){
        document.getElementById("quick-status").textContent = "Desktop unlocked. Use the start menu or cards to open apps.";
      }
      log("Closed window: " + which);
    }
    function bringToFront(el){
      document.querySelectorAll(".window").forEach(w=>w.style.zIndex=10);
      el.style.zIndex = 20;
    }
    function renderTaskbar(){
      const container = document.getElementById("task-apps");
      container.innerHTML = "";
      openWindows.forEach(w=>{
        const btn = document.createElement("div");
        btn.className = "task-pill";
        btn.textContent = prettyName(w);
        btn.onclick = ()=>openWindow(w);
        container.appendChild(btn);
      });
    }
    function prettyName(w){
      if(w==="arcade") return "Arcade";
      if(w==="admin") return "Admin";
      if(w==="chat") return "Chat";
      if(w==="profile") return "Profile";
      if(w==="settings") return "Settings";
      return w;
    }

    // START MENU
    function toggleStart(){
      if(!currentUser){
        alert("You must log in first.");
        return;
      }
      const menu = document.getElementById("start-menu");
      menu.style.display = (menu.style.display === "flex" || menu.style.display === "block") ? "none" : "flex";
    }
    function closeStart(){
      document.getElementById("start-menu").style.display = "none";
    }
    function openFromStart(which){
      openWindow(which);
    }

    // PROFILE XP
    let profileLevel = 1;
    let profileXP = 0;
    let profileXPMax = 100;

    function updateProfileUI(){
      document.getElementById("profile-level").textContent = profileLevel;
      document.getElementById("profile-xp").textContent = profileXP;
      document.getElementById("profile-xp-max").textContent = profileXPMax;
      const pct = Math.min(100, (profileXP/profileXPMax)*100);
      document.getElementById("profile-xp-bar").style.width = pct + "%";
    }
    updateProfileUI();

    function addXP(amount){
      profileXP += amount;
      while(profileXP >= profileXPMax){
        profileXP -= profileXPMax;
        profileLevel += 1;
        profileXPMax = Math.min(profileXPMax + 50, 65465365); // nível máximo absurdo só pela piada
        log("Level up! New level: " + profileLevel);
      }
      updateProfileUI();
    }

    // ARCADE
    function launchGame(name, genre){
      gamesLaunched += 1;
      document.getElementById("admin-games").textContent = gamesLaunched;
      log("Launched game: " + name + " (" + genre + ")");
      addXP(20);
      openWindow("profile");
    }

    // CHAT
    function sendChat(){
      if(!currentUser){
        alert("You must log in first.");
        return;
      }
      const input = document.getElementById("chat-input");
      const text = input.value.trim();
      if(!text) return;
      const box = document.getElementById("chat-box");
      const div = document.createElement("div");
      div.className = "chat-msg";
      const meta = document.createElement("div");
      meta.className = "chat-meta";
      meta.textContent = currentUser + " • " + new Date().toLocaleTimeString();
      const body = document.createElement("div");
      body.textContent = text;
      div.appendChild(meta);
      div.appendChild(body);
      box.appendChild(div);
      box.scrollTop = box.scrollHeight;
      input.value = "";
      chatMessages += 1;
      document.getElementById("admin-chat").textContent = chatMessages;
      log("Chat message from " + currentUser + ": " + text);
    }

    // SETTINGS
    function toggleClass(elId){
      document.getElementById(elId).classList.toggle("on");
    }
    function toggleLight(){
      toggleClass("toggle-light");
      const root = document.documentElement;
      const isOn = document.getElementById("toggle-light").classList.contains("on");
      if(isOn){
        root.style.setProperty("--bg-main","#f9fafb");
        root.style.setProperty("--bg-window","#f9fafb");
        root.style.setProperty("--text-main","#020617");
        root.style.setProperty("--text-soft","#4b5563");
        document.getElementById("widget-mode").textContent = "Light • Blue accent";
      }else{
        root.style.setProperty("--bg-main","#020617");
        root.style.setProperty("--bg-window","#020617");
        root.style.setProperty("--text-main","#e5e7eb");
        root.style.setProperty("--text-soft","#9ca3af");
        document.getElementById("widget-mode").textContent = "Dark • Blue accent";
      }
      log("Light mode " + (isOn ? "enabled" : "disabled") + ".");
    }
    function toggleGreen(){
      toggleClass("toggle-green");
      const root = document.documentElement;
      const isOn = document.getElementById("toggle-green").classList.contains("on");
      if(isOn){
        root.style.setProperty("--accent","#22c55e");
        root.style.setProperty("--accent-soft","rgba(34,197,94,0.18)");
        document.getElementById("widget-mode").textContent =
          (document.getElementById("widget-mode").textContent.includes("Light") ? "Light" : "Dark") + " • Green accent";
      }else{
        root.style.setProperty("--accent","#38bdf8");
        root.style.setProperty("--accent-soft","rgba(56,189,248,0.18)");
        document.getElementById("widget-mode").textContent =
          (document.getElementById("widget-mode").textContent.includes("Light") ? "Light" : "Dark") + " • Blue accent";
      }
      log("Accent color switched to " + (isOn ? "green" : "blue") + ".");
    }
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
