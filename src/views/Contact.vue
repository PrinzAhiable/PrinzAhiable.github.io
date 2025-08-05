<template>
  <section class="contact" data-aos="fade-up">
    <h1 data-aos="zoom-in">Get In Touch</h1>
    <p class="intro" data-aos="fade-up" data-aos-delay="100">
      Have a project in mind? I’d love to hear from you. Let’s create something amazing
      together.
    </p>

    <div class="contact-content">
      <div class="contact-info" data-aos="fade-right" data-aos-delay="200">
        <h2>Let's Connect</h2>
        <ul>
          <li>
            <i class="fas fa-envelope"></i> <span>Email</span><br />
            <a href="mailto:ahiableprinz@gmail.com" class="contact-link">
              ahiableprinz@gmail.com
            </a>
          </li>
          <li>
            <i class="fas fa-phone"></i> <span>Phone</span><br />
            <a href="tel:+233554948718" class="contact-link"> +233 554 948 718 </a>
          </li>
          <li>
            <i class="fas fa-map-marker-alt"></i> <span>Location</span><br />
            <a
              href="https://www.google.com/maps/search/?api=1&query=Ho+Volta+Region+Ghana"
              target="_blank"
              rel="noopener noreferrer"
              class="contact-link"
            >
              Ho , Volta Region , Ghana
            </a>
          </li>
        </ul>

        <div class="follow-me" data-aos="fade-up" data-aos-delay="300">
          <h3>Follow Me</h3>
          <div class="social-icons">
            <a
              href="https://www.linkedin.com/in/ahiable-prinz/"
              target="_blank"
              aria-label="LinkedIn"
            >
              <i class="fab fa-linkedin"></i>
            </a>
            <a href="https://github.com/PrinzAhiable" target="_blank" aria-label="GitHub">
              <i class="fab fa-github"></i>
            </a>
            <a
              href="https://twitter.com/yourusername"
              target="_blank"
              aria-label="Twitter"
            >
              <i class="fab fa-twitter"></i>
            </a>
          </div>
        </div>
      </div>

      <form class="contact-form" data-aos="fade-left" data-aos-delay="400">
        <h2>Send Message</h2>
        <div class="form-group">
          <input type="text" placeholder="Your name" required />
          <input type="email" placeholder="your.email@example.com" required />
        </div>
        <input type="text" placeholder="What's this about?" required />
        <textarea
          placeholder="Tell me about your project or just say hello..."
          rows="5"
          required
        ></textarea>
        <button type="submit" class="full-width">Send Message</button>
      </form>
    </div>
  </section>
</template>

<script>
import AOS from "aos";
import "aos/dist/aos.css";

export default {
  name: "Contact",
  mounted() {
    AOS.init({
      duration: 800,
      once: false,
    });
  },
};
</script>

<style scoped>
.contact {
  background: #0b0b1f;
  color: #fff;
  padding: 4rem 2rem;
  text-align: center;
}

.intro {
  max-width: 600px;
  margin: 0 auto 3rem;
  font-size: 0.95rem;
}

.contact-link {
  color: #fff;
  text-decoration: none;
  transition: color 0.3s;
}

.contact-link:hover {
  color: #7d5fff;
  text-decoration: underline;
}

.contact-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  max-width: 1000px;
  margin: 0 auto;
}

.contact-info {
  text-align: left;
}

.contact-info h2 {
  margin-bottom: 1rem;
}

.contact-info ul {
  list-style: none;
  padding: 0;
  margin-bottom: 1rem;
}

.contact-info li {
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.contact-info i {
  color: #7d5fff;
  margin-right: 0.5rem;
}

.contact-info span {
  font-weight: bold;
}

.follow-me {
  margin-top: 1rem;
}

.follow-me h3 {
  margin-bottom: 0.5rem;
}

.social-icons {
  display: flex;
  gap: 1rem;
}

.social-icons a {
  color: #fff;
  font-size: 1.5rem;
  transition: color 0.3s;
}

.social-icons a:hover {
  color: #7d5fff;
}

.contact-form {
  background: #161636;
  padding: 2rem;
  border-radius: 10px;
  text-align: left;
}

.contact-form h2 {
  margin-bottom: 1rem;
}

.form-group {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

input,
textarea {
  width: 100%;
  padding: 0.75rem;
  margin-bottom: 1rem;
  border: none;
  border-radius: 5px;
  background: #1e1e3f;
  color: white;
  font-size: 0.9rem;
}

button.full-width {
  width: 100%;
  padding: 0.75rem 1.5rem;
  background: #7d5fff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

@media (min-width: 768px) {
  .contact-content {
    flex-direction: row;
    justify-content: space-between;
  }

  .contact-info {
    width: 40%;
  }

  .contact-form {
    width: 55%;
  }
}
</style>
