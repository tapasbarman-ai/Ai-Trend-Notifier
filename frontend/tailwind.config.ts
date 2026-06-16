import type { Config } from 'tailwindcss'

const config: Config = {
    content: [
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
        './app/**/*.{js,ts,jsx,tsx,mdx}',
    ],
    theme: {
        extend: {
            backgroundImage: {
                'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
                'gradient-conic':
                    'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
            },
            colors: {
                primary: '#6366f1', // Indigo 500
                secondary: '#4f46e5', // Violet-Indigo
                accent: '#a855f7', // Violet 500
                darkBg: '#030712', // Deep Space Slate 950
                cardBg: 'rgba(17, 24, 39, 0.5)', // Translucent Card
                borderGray: 'rgba(255, 255, 255, 0.06)' // Translucent borders
            }

        },
    },
    plugins: [],
}
export default config
