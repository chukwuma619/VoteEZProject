/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "templates/*.html",
    'static/JS/script.js',
  ],
  theme: {
    extend: {
      flexBasis: {
        'form': "calc(50% - 0.75rem)",
      }
    }
  },
  plugins: [],
}

