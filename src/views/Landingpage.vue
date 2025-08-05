<template>
  <div class="landing-page">
    <Navbar />

    <!-- Each section has an ID for anchor navigation -->
    <section id="home">
      <Home />
    </section>

    <section id="about">
      <About />
    </section>

    <section id="projects">
      <Projects />
    </section>

    <section id="skills">
      <Skills />
    </section>

    <section id="contact">
      <Contact />
    </section>
  </div>
</template>

<script setup>
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Projects from "../views/Projects.vue";
import Skills from "../views/Skills.vue";
import Contact from "../views/Contact.vue";
</script>

<style scoped>
.landing-page {
  scroll-behavior: smooth; /* Enables smooth scrolling for anchor links */
}
</style>
