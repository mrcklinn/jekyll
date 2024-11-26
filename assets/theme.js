document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const controlPanel = document.querySelector('.control-panel');
    const controlPanelToggle = document.querySelector('.control-panel-toggle');
    
    // Initialize theme
    const initialTheme = document.documentElement.getAttribute('data-theme');
    const savedTheme = localStorage.getItem('theme') || initialTheme || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    themeToggle.textContent = savedTheme === 'dark' ? '●' : '○';
    
    // Theme toggle
    themeToggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        themeToggle.textContent = newTheme === 'dark' ? '●' : '○';
    });
    
    // Control panel toggle
    controlPanelToggle.addEventListener('click', () => {
        controlPanel.classList.toggle('open');
    });
}); 