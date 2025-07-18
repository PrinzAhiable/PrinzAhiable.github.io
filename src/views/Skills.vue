<template>
  <div class="skills-page" data-aos="fade-up">
    <h1>My Skills</h1>
    <div class="skills-grid">
      <div
        v-for="(skill, index) in skills"
        :key="index"
        class="skill-card"
        data-aos="zoom-in"
        :data-aos-delay="index * 100"
      >
        <img :src="skill.icon" :alt="skill.name" class="skill-icon" />
        <p class="skill-name">{{ skill.name }}</p>
        <p class="skill-description">{{ skill.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import AOS from "aos";
import "aos/dist/aos.css";

export default {
  name: "Skills",
  data() {
    return {
      skills: [
        {
          name: "HTML",
          icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",
          description: "Markup language for structuring web pages.",
        },
        {
          name: "CSS",
          icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg",
          description: "Used to style and layout web elements.",
        },
        {
          name: "JavaScript",
          icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
          description: "Adds interactivity and logic to web apps.",
        },
        {
          name: "Vue.js",
          icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg",
          description: "Progressive JavaScript framework for building UIs.",
        },
        {
          name: "Node.js",
          icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg",
          description: "JavaScript runtime for building backend services.",
        },
        {
          name: "Git",
          icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg",
          description: "Version control system for tracking code changes.",
        },
        {
          name: "GitHub",
          icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg",
          description: "Cloud-based platform for hosting Git repositories.",
        },
      ],
    };
  },
  mounted() {
    AOS.init({ duration: 800 });
  },
};
</script>

<style scoped>
.skills-page {
  padding: 4rem 2rem;
  text-align: center;
  background: linear-gradient(135deg, #0e0e2c, #1f1f47);
  color: white;
  min-height: 100vh;
}

h1 {
  font-size: 2.2rem;
  margin-bottom: 2rem;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 2rem;
  align-items: stretch;
  justify-content: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.skill-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(8px);
  padding: 1.5rem 1rem;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  min-height: 180px;
}

.skill-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.skill-icon {
  width: 48px;
  height: 48px;
  margin-bottom: 0.75rem;
}

.skill-name {
  color: #f0c330;
  font-weight: bold;
  font-size: 1rem;
}

.skill-description {
  color: #ddd;
  font-size: 0.85rem;
  text-align: center;
  margin-top: 0.5rem;
  line-height: 1.3;
}

@media (max-width: 600px) {
  .skills-grid {
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
    gap: 1rem;
  }

  .skill-icon {
    width: 36px;
    height: 36px;
  }

  .skill-name {
    font-size: 0.9rem;
  }

  .skill-description {
    font-size: 0.75rem;
  }
}
</style>
