import type { Metadata } from 'next'
import { Inter, Plus_Jakarta_Sans } from 'next/font/google'
import './globals.css'
import Navbar from '@/components/Navbar'

const inter = Inter({ 
    subsets: ['latin'],
    variable: '--font-inter',
})

const plusJakartaSans = Plus_Jakarta_Sans({ 
    subsets: ['latin'],
    variable: '--font-plus-jakarta',
})

export const metadata: Metadata = {
    title: 'AI Insights',
    description: 'Stay ahead of the curve with the latest AI trends.',
}

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <html lang="en">
            <body className={`${inter.variable} ${plusJakartaSans.variable} font-sans`}>
                <Navbar />
                <main className="pt-20 min-h-screen">
                    {children}
                </main>
            </body>
        </html>
    )
}

