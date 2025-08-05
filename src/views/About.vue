<template>
  <section class="about">
    <h1 class="section-title" data-aos="fade-down">About Me</h1>
    <div class="content">
      <div class="about-image-container" data-aos="zoom-in">
        <div class="about-image">
          <img :src="aboutImage" alt="my picture" />
        </div>
        <a
          href="/resume.pdf"
          download
          class="download-btn"
          data-aos="fade-up"
          data-aos-delay="200"
        >
          Download Resume
        </a>
      </div>

      <div class="about-text" data-aos="fade-left">
        <h2>Passionate Developer & Designer</h2>
        <p data-aos="fade-up" data-aos-delay="100">
          With over 3 years of experience in web development, I specialize in creating
          modern, responsive applications that deliver exceptional user experiences.
        </p>
        <p data-aos="fade-up" data-aos-delay="200">
          I believe in the power of clean code, intuitive design, and continuous learning.
          When I'm not coding, you can find me exploring new technologies, contributing to
          open-source projects.
        </p>
        <div class="stats">
          <div class="stat" data-aos="flip-left">
            <strong>5+</strong><br />Projects Completed
          </div>
          <div class="stat" data-aos="flip-left" data-aos-delay="100">
            <strong>3+</strong><br />Years Experience
          </div>
          <div class="stat red" data-aos="flip-left" data-aos-delay="200">
            <strong>10+</strong><br />Happy Clients
          </div>
          <div class="stat blue" data-aos="flip-left" data-aos-delay="300">
            <strong>24/7</strong><br />Support
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from "vue";
import AOS from "aos";
import "aos/dist/aos.css";

import aboutImage from "../assets/images/my image.jpg";


//  Using my LinkedIn image URL directly
//const aboutImage = "";

onMounted(() => {
  AOS.init({
    duration: 800,
    once: false,
  });
});
</script>

<style scoped>
.about {
  background: linear-gradient(135deg, #0e0e2c, #1f1f47);
  color: #fff;
  padding: 4rem 1.5rem;
  min-height: 100vh;
  backdrop-filter: blur(10px);
}

.section-title {
  text-align: center;
  font-size: 2rem;
  position: relative;
  margin-bottom: 3rem;
}

.section-title::after {
  content: "";
  display: block;
  width: 60px;
  height: 3px;
  background: rgba(255, 255, 255, 0.3);
  margin: 0.5rem auto 0;
}

.content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  max-width: 1000px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 2rem;
  backdrop-filter: blur(12px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
}

@media (min-width: 768px) {
  .content {
    flex-direction: row;
    align-items: flex-start;
  }

  .about-image-container {
    flex: 0 0 40%;
  }

  .about-text {
    flex: 1;
    padding-left: 2rem;
  }
}

.about-image-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.about-image {
  width: 100%;
  height: auto;
  max-width: 350px;
  aspect-ratio: 1 / 1;
  margin: 0 auto;
  overflow: hidden;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
  border: 2px solid rgba(255, 255, 255, 0.2);
}

.about-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  border-radius: 12px;
}

.download-btn {
  background-color: #a29bfe;
  color: #0e0e2c;
  text-decoration: none;
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
  text-align: center;
}

.download-btn::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.1);
  transition: left 0.3s ease;
}

.download-btn:hover::before {
  left: 0;
}

.download-btn:hover {
  background-color: #7a75f5;
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 6px 16px rgba(122, 117, 245, 0.4);
  color: #fff;
}

.about-text {
  text-align: left;
}

.about-text h2 {
  color: #a29bfe;
  margin-bottom: 1rem;
  font-size: 1.4rem;
}

.about-text p {
  margin-bottom: 1rem;
  font-size: 0.95rem;
  line-height: 1.6;
  color: #ddd;
}

.stats {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 1.5rem;
}

.stat {
  background: rgba(255, 255, 255, 0.07);
  padding: 1rem;
  flex: 1 1 100%;
  text-align: center;
  border-radius: 12px;
  backdrop-filter: blur(8px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

@media (min-width: 480px) {
  .stat {
    flex: 1 1 45%;
  }
}

@media (min-width: 768px) {
  .stat {
    flex: 1 1 40%;
  }
}

.stat strong {
  font-size: 1.2rem;
  display: block;
  margin-bottom: 0.25rem;
  color: #fff;
}

.stat.red strong {
  color: #ff6b6b;
}

.stat.blue strong {
  color: #4dabf7;
}
</style>
