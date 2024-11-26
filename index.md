---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

  <style>
    .intro-section {
      display: flex;
      border: 2px solid #e8e8e8;
      padding: 20px;    
      max-width: 800px;
      margin-top: 20px;
      align-items: center;
      gap: 20px;
      opacity: 0;
      transform: translateY(20px);
      animation: fadeInUp 0.8s ease forwards;
    }
    .intro-section img {
      max-width: 350px;
      opacity: 0;
      transform: scale(0.95);
      animation: fadeInScale 0.008s ease 0.002s forwards;
    }
    .intro-section p {
      margin: 0;
      font-size: 32px;
      opacity: 0;
      transform: translateX(-20px);
      animation: fadeInSlide 0.8s ease 0.4s forwards;
    }
    .intro-section .enjoy {
      margin: 0;
      padding-top: 15px;
      font-size: 20px;
      opacity: 0;
      transform: translateX(-20px);
      animation: fadeInSlide 0.8s ease 0.6s forwards;
    }
    .intro-section .pronouns {
      margin: 0;
      padding-top: 0px;
      font-size: 15px;
      display: block;
      color: #888;
      opacity: 0;
      transform: translateX(-20px);
      animation: fadeInSlide 0.8s ease 0.8s forwards;
    }

    /* Responsive adjustments */
    @media (max-width: 600px) {
      .intro-section {
        flex-direction: column;
        align-items: flex-start;
      }
      .intro-section img {
        max-width: 100%;
      }
      .intro-section p {
        font-size: 24px;
      }
      .intro-section .enjoy {
        font-size: 18px;
      }
    }

    @keyframes fadeInUp {
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @keyframes fadeInScale {
      to {
        opacity: 1;
        transform: scale(1);
      }
    }

    @keyframes fadeInSlide {
      to {
        opacity: 1;
        transform: translateX(0);
      }
    }

/* Timeline CSS */
.timeline-wrapper {
  padding: 40px 20px;
  max-width: 800px;
  margin: 0 auto;
}

.timeline {
  position: relative;
  padding: 20px 0;
}

.timeline::before {
  content: '';
  position: absolute;
  width: 3px;
  background: linear-gradient(180deg, #e8e8e8 0%, #d1d1d1 100%);
  top: 0;
  bottom: 0;
  left: 50px;
}

.timeline-item {
  margin: 40px 0;
  position: relative;
  padding-left: 70px;
}

.timeline-item::before {
  content: '';
  position: absolute;
  width: 12px;
  height: 12px;
  background: white;
  border: 3px solid #e8e8e8;
  border-radius: 50%;
  left: 44px;
  top: 50%;
  transform: translateY(-50%);
  transition: all 0.3s ease;
}

.timeline-item:hover::before {
  background: #e8e8e8;
}

.timeline-content {
  background: white;
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  padding: 20px;
  position: relative;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 20px;
}

.timeline-content:hover {
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transform: translateX(5px);
}

.timeline-logo {
  width: 60px;
  height: 40px;
  object-fit: contain;
}

.timeline-text {
  flex: 1;
}

.timeline-date {
  font-size: 14px;
  color: #666;
  margin-bottom: 8px;
}

.timeline-description {
  margin: 0;
  line-height: 1.5;
}

@media (max-width: 600px) {
  .timeline::before {
    left: 30px;
  }
  
  .timeline-item {
    padding-left: 50px;
  }
  
  .timeline-item::before {
    left: 24px;
  }
}
</style>

<!--Body-->
  <main class="page-content" aria-label="Content">
    <div class="wrapper">
      <div class="intro-section">
        <img src="/assets/images/profile.jpg" alt="Neha Balamurugan">
        <div class="wrapper">
            <p> Hi, I'm Neha👋🏾 </p>  
            <p class="pronouns">[NAY-ha](she/her/hers)</p>
            <p class= "enjoy">I'm a computer science student interested in VR/AR, ML and entreprenuership. Welcome to my personal website where I share my projects, career, and more!</p>
            <p class="enjoy">I like: 🎾 👩🏾‍💻 🧄 🏋🏾‍♀️ 🦦 🌵</p>
        </div>
      </div>
    </div>
    <div class="wrapper">
      <div class="timeline-wrapper">
        <div class="timeline">
          <article class="timeline-item">
            <div class="timeline-content">
              <img src="/assets/images/stanford-logo.webp" alt="Stanford" class="timeline-logo">
              <div class="timeline-text">
                <div class="timeline-date">2024-2026</div>
                <p class="timeline-description">
                  Pursuing a MSc in Computer Science at Stanford University with a concentration in Artificial Intelligence.
                </p>
              </div>
            </div>
          </article>

          <article class="timeline-item">
            <div class="timeline-content">
              <img src="/assets/images/asu-logo.png" alt="ASU" class="timeline-logo">
              <div class="timeline-text">
                <div class="timeline-date">2021-2024</div>
                <p class="timeline-description">
                  Graduated Summa Cum Laude from Arizona State University with BSc in Computer Science as an Outstanding Graduate. Researched Virtual Reality at the <a href="https://meteor.ame.asu.edu/">Meteor Studio</a>, and Augmented Reality at <a href="https://hcistudio.org/">HCIstudio</a>. Won a few hackathons and won even fewer club tennis tournaments.
                </p>
              </div>
            </div>
          </article>

          <article class="timeline-item">
            <div class="timeline-content">
              <img src="/assets/images/mtn-logo.jpeg" alt="Mountain Ridge" class="timeline-logo">
              <div class="timeline-text">
                <div class="timeline-date">2017-2021</div>
                <p class="timeline-description">
                  Finished as the Valedictorian of Mountain Ridge High School in 2021 where I played better tennis, took too many APs, and founded <a href="https://www.yourvalley.net/stories/mountain-ridge-students-help-break-digital-divide,181284">Break Digital Divide</a>.
                </p>
              </div>
            </div>
          </article>
        </div>
      </div>
    </div>
  </main>


  <!--Footer-->
  <footer class="site-footer h-card">
    <data class="u-url" href="/"></data>
    <div class="wrapper">
      <h2 class="footer-heading">Neha Balamurugan</h2>
      <div class="footer-col-wrapper">
        <div class="footer-col footer-col-1">
          <ul class="contact-list">
            <li class="p-name">Neha Balamurugan</li>
            <li><a class="u-email" href="mailto:nbalamuru@gmail.com">nbalamuru@gmail.com</a></li>
          </ul>
        </div>
        <div class="footer-col footer-col-2">
          <ul class="social-media-list">
            <li><a href="https://github.com/nehabalamurugan"><svg class="svg-icon"><use xlink:href="/assets/minima-social-icons.svg#github"></use></svg> <span class="username">nehabalamurugan</span></a></li>
            <li><a href="https://www.linkedin.com/in/neha-balamurugan-8455981b1/"><svg class="svg-icon"><use xlink:href="/assets/minima-social-icons.svg#linkedin"></use></svg> <span class="username">nehabalamurugan</span></a></li>
          </ul>
        </div>
        <div class="footer-col footer-col-3">
          <p>Neha Balamurugan&#39;s personal website</p>
        </div>
      </div>
    </div>
  </footer>

