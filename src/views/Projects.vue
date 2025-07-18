<template>
  <section class="projects" data-aos="fade-up">
    <h1 class="section-title" data-aos="fade-up" data-aos-delay="100">Projects</h1>

    <div class="project-grid">
      <div
        v-for="(project, index) in projects"
        :key="project.title"
        class="project-card"
        :data-aos="'zoom-in'"
        :data-aos-delay="100 * (index + 1)"
      >
        <div class="card-header" :style="{ background: project.headerColor }">
          <h2>{{ project.title }}</h2>
        </div>

        <div class="card-body">
          <h3>{{ project.subtitle }}</h3>
          <p>{{ project.description }}</p>

          <div class="tech-stack">
            <span v-for="tech in project.tech" :key="tech" class="badge">
              {{ tech }}
            </span>
          </div>

          <div class="card-actions">
            <a
              class="btn live"
              :href="project.demo"
              target="_blank"
              rel="noopener noreferrer"
            >
              Live Demo
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import AOS from "aos";
import "aos/dist/aos.css";

export default {
  name: "Projects",
  data() {
    return {
      projects: [
        {
          title: "E-commerce",
          subtitle: "E-commerce Platform",
          description: "Modern shopping experience with Vue.js",
          headerColor: "linear-gradient(to bottom, #ff6600, #1e1e1e)",
          tech: ["Vue.js", "CSS3", "JavaScript"],
          demo: "#",
        },
        {
          title: "Dashboard",
          subtitle: "SaaS Dashboard",
          description: "Clean admin interface with real-time data",
          headerColor: "linear-gradient(to bottom, #00e6ff, #1e1e1e)",
          tech: ["HTML5", "Vue.js", "CSS3"],
          demo: "#",
        },
        {
          title: "Corporate",
          subtitle: "Corporate Website",
          description: "Professional business presence",
          headerColor: "linear-gradient(to bottom, #ffeb3b, #1e1e1e)",
          tech: ["JavaScript", "CSS3", "HTML5"],
          demo: "#",
        },
        {
          title: "Portfolio",
          subtitle: "Personal Portfolio",
          description: "Showcase of my work and skills",
          headerColor: "linear-gradient(to bottom, #8e44ad, #1e1e1e)",
          tech: ["Vue.js", "SCSS", "GSAP"],
          demo: "https://prinzahiable.github.io/",
        },
        {
          title: "Blog App",
          subtitle: "Content Management",
          description: "Blogging platform with admin tools",
          headerColor: "linear-gradient(to bottom, #2ecc71, #1e1e1e)",
          tech: ["Vue", "Node.js", "MongoDB"],
          demo: "#",
        },
        {
          title: "Landing Page",
          subtitle: "Marketing Site",
          description: "Conversion-focused design",
          headerColor: "linear-gradient(to bottom, #3498db, #1e1e1e)",
          tech: ["HTML5", "CSS3", "Bootstrap"],
          demo: "#",
        },
        {
          title: "To-Do App",
          subtitle: "Task Manager",
          description: "Simple and intuitive task management",
          headerColor: "linear-gradient(to bottom, #f39c12, #1e1e1e)",
          tech: ["Vue.js", "LocalStorage", "CSS"],
          demo: "#",
        },
        {
          title: "Weather App",
          subtitle: "Real-Time Weather",
          description: "Live weather data with a responsive UI",
          headerColor: "linear-gradient(to bottom, #2980b9, #1e1e1e)",
          tech: ["Vue", "OpenWeatherMap API", "SCSS"],
          demo: "#",
        },
      ],
    };
  },
  mounted() {
    AOS.init({
      duration: 800,
      once: false,
      easing: "ease-out",
    });
  },
};
</script>

<style scoped>
.projects {
  background: linear-gradient(135deg, #0e0e2c, #1f1f47);
  padding: 3rem 1.5rem;
  color: #fff;
  text-align: center;
  min-height: 100vh;
}

.section-title {
  font-size: 2rem;
  color: #a4ffaf;
  margin-bottom: 3rem;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  align-items: stretch;
}

.project-card {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  display: flex;
  flex-direction: column;
  height: 100%;
  transition: transform 0.3s ease;
}

.project-card:hover {
  transform: translateY(-5px);
}

.card-header {
  padding: 2rem 1rem;
  color: #fff;
  font-weight: bold;
  font-size: 1.5rem;
  text-align: center;
}

.card-body {
  padding: 1.5rem 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: center;
  flex-grow: 1;
}

.card-body h3 {
  font-weight: bold;
  margin-bottom: 0.5rem;
  color: #fff;
  font-size: 1.1rem;
}

.card-body p {
  font-size: 0.95rem;
  margin-bottom: 1rem;
  color: #ddd;
}

.tech-stack {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.badge {
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
  padding: 0.3rem 0.7rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 600;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.card-actions {
  display: flex;
  justify-content: center;
  margin-top: auto;
}

.btn {
  padding: 0.5rem 1.2rem;
  font-weight: bold;
  font-size: 0.85rem;
  border-radius: 5px;
  text-decoration: none;
  display: inline-block;
  transition: 0.3s ease-in-out;
}

.btn.live {
  background: rgba(255, 87, 51, 0.8);
  color: #fff;
  backdrop-filter: blur(6px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.btn.live:hover {
  background: rgba(255, 112, 77, 0.95);
}

@media (max-width: 480px) {
  .section-title {
    font-size: 1.5rem;
  }

  .card-body h3 {
    font-size: 1rem;
  }

  .card-body p {
    font-size: 0.85rem;
  }

  .btn {
    font-size: 0.75rem;
  }

  .card-header {
    font-size: 1.2rem;
  }

  .badge {
    font-size: 0.75rem;
  }
}
</style>
