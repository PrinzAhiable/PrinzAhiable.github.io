<template>
  <nav class="navbar">
    <!-- Toggle Button for Mobile -->
    <button class="toggle-btn" @click="showNav = !showNav" aria-label="Toggle Navigation">
      ☰
    </button>

    <div class="nav-container">
      <div class="logo">Prince's Portfolio</div>

      <!-- Navigation Links -->
     <div class="nav-links" :class="{ show: showNav }">
  <a href="#home" @click="hideNav">Home</a>
  <a href="#about" @click="hideNav">About</a>
  <a href="#projects" @click="hideNav">Projects</a>
  <a href="#skills" @click="hideNav">Skills</a>
  <a href="#contact" @click="hideNav">Contact</a>
</div>

    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';

const showNav = ref(false);

function hideNav() {
  showNav.value = false;
}
</script>

<style scoped>
/* ===== Base Navbar Styles ===== */
.navbar {  background: linear-gradient(135deg, #0e0e2c, #1f1f47);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  position: sticky;
  top: 0;
  z-index: 1000;
  padding: 1rem 0;
}

/* ===== Toggle Button for Mobile ===== */
.toggle-btn {
  position: fixed;
  top: 1rem;
  left: 1rem;
  font-size: 1.8rem;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 8px;
  cursor: pointer;
  z-index: 1100;
  backdrop-filter: blur(4px);
}

/* ===== Nav Container ===== */
.nav-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  transition: all 0.3s ease;
}

.logo {
  color: white;
  font-size: 1.4rem;
  font-weight: bold;
  margin-bottom: 1rem;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  text-align: center;
}

/* ===== Nav Links - Mobile ===== */
.nav-links {
  display: none;
  flex-direction: column;
  gap: 0.75rem;
  text-align: center;
  width: 100%;
  transition: max-height 0.3s ease-in-out;
  overflow: hidden;
}

.nav-links.show {
  display: flex;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: 500;
  font-size: 1rem;
  transition: color 0.3s ease, transform 0.3s ease;
}

.nav-links a:hover {
  color: #a29bfe;
  transform: translateY(-2px);
}

/* ===== Responsive for Desktop (768px+) ===== */
@media (min-width: 768px) {
  .toggle-btn {
    display: none;
  }

  .nav-container {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }

  .logo {
    margin-bottom: 0;
  }

  .nav-links {
    display: flex !important;
    flex-direction: row;
    justify-content: flex-end;
    gap: 1.5rem;
    width: auto;
  }
}
</style>
