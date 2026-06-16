import type { Config } from 'tailwindcss'

const config: Config = {
    content: [
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
        './app/**/*.{js,ts,jsx,tsx,mdx}',
    ],
    theme: {
        extend: {
            colors: {
                background: '#f9f9ff',
                'on-background': '#151c27',
                primary: '#705d00',
                'primary-container': '#ffd700',
                'on-primary-container': '#705e00',
                secondary: '#5f5e5f',
                'surface-container-lowest': '#ffffff',
                'surface-container-low': '#f0f3ff',
                'surface-container': '#e7eefe',
                'surface-container-high': '#e2e8f8',
                'surface-container-highest': '#dce2f3',
                'on-surface-variant': '#4d4732',
                'outline-variant': '#d0c6ab',
                'inverse-surface': '#2a313d',
                'inverse-on-surface': '#ebf1ff',
                error: '#ba1a1a',
                'error-container': '#ffdad6',
                'on-error-container': '#93000a',
            },
            fontFamily: {
                sans: ['var(--font-inter)', 'sans-serif'],
                display: ['var(--font-plus-jakarta)', 'sans-serif'],
            },
            fontSize: {
                'caption': ['12px', { lineHeight: '16px', fontWeight: '400' }],
                'headline-md': ['24px', { lineHeight: '32px', fontWeight: '700' }],
                'headline-lg-mobile': ['32px', { lineHeight: '40px', fontWeight: '700' }],
                'body-md': ['16px', { lineHeight: '24px', fontWeight: '400' }],
                'label-bold': ['14px', { lineHeight: '20px', letterSpacing: '0.05em', fontWeight: '600' }],
                'headline-lg': ['40px', { lineHeight: '48px', letterSpacing: '-0.01em', fontWeight: '700' }],
                'display-xl': ['64px', { lineHeight: '72px', letterSpacing: '-0.02em', fontWeight: '800' }],
                'body-lg': ['18px', { lineHeight: '28px', fontWeight: '400' }],
            },
            spacing: {
                'margin-desktop': '64px',
                'margin-mobile': '20px',
                'gutter': '24px',
                'container-max-width': '1280px',
            }


        },
    },
    plugins: [],
}
export default config
