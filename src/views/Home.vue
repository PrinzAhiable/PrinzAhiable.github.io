<template>
  <section class="home">
    <div class="container" ref="container">
      <div class="profile-image">Profile</div>
      <h1><span class="name-highlight">Frontend Developer</span></h1>
      <h2>Full Stack Developer &amp; UI/UX Designer</h2>
      <p class="intro">Passionate about creating innovative digital solutions...</p>

      <div class="buttons">
        <router-link to="/projects" class="btn primary">View My Work</router-link>
        <router-link to="/contact" class="btn secondary">Get In Touch</router-link>
      </div>

      <div class="socials">
        <a href="mailto:ahiableprinz@gmail.com" aria-label="Gmail">
          <img
            src="https://img.icons8.com/color/48/gmail-new.png"
            alt="Gmail"
            class="gmail-icon"
          />
        </a>
        <a href="https://www.linkedin.com/in/ahiable-prinz/" aria-label="LinkedIn"
          ><i class="fab fa-linkedin"></i
        ></a>
        <a href="https://github.com/PrinzAhiable" aria-label="GitHub"
          ><i class="fab fa-github"></i
        ></a>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

const container = ref(null);

onMounted(() => {
  const items = container.value.querySelectorAll(
    ".profile-image, h1, h2, .intro, .buttons, .socials"
  );

  gsap.from(items, {
    opacity: 0,
    y: 30,
    duration: 0.8,
    stagger: 0.2,
    ease: "power3.out",
    scrollTrigger: {
      trigger: container.value,
      start: "top 80%",
    },
  });
});
</script>

<style scoped>
.home {
  background: linear-gradient(135deg, #0e0e2c, #1f1f47);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 3rem 1.5rem;
  color: #fff;
}

.container {
  max-width: 600px;
  text-align: center;
}

.profile-image {
  width: 100px;
  height: 100px;
  margin: 1rem auto;
  border-radius: 50%;
  background: #4b00ff;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 3px solid #fff;
  font-weight: bold;
  font-size: 1rem;
}

.name-highlight {
  color: #33d9b2;
}

h1 {
  font-size: 2rem;
  margin: 0.5rem 0;
}

h2 {
  font-size: 1.3rem;
  font-weight: 300;
}

.intro {
  margin: 1rem 0 2rem;
  font-size: 0.95rem;
  line-height: 1.6;
}

.buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2rem;
}

@media (min-width: 600px) {
  .buttons {
    flex-direction: row;
    justify-content: center;
  }
}

.btn {
  padding: 0.75rem 1.5rem;
  border-radius: 5px;
  font-weight: bold;
  font-size: 1rem;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.3s ease-in-out;
}

.primary {
  background: #7d5fff;
  color: #fff;
}

.secondary {
  background: transparent;
  border: 2px solid #7d5fff;
  color: #7d5fff;
}

.primary:hover {
  box-shadow: 0 0 20px #a29bfe;
}

.secondary:hover {
  background: #7d5fff;
  color: #fff;
  box-shadow: 0 0 20px #7d5fff;
}

.socials {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.socials a {
  color: #fff;
  font-size: 1.5rem;
  transition: color 0.3s ease-in-out;
}

.socials a:hover {
  color: #7d5fff;
}

.gmail-icon {
  width: 24px;
  height: 24px;
  filter: brightness(0) invert(1);
  transition: transform 0.3s ease, filter 0.3s ease;
}

.socials a:hover .gmail-icon {
  transform: scale(1.1);
  filter: none;
}
</style>
