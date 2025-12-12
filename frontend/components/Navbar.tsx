import Link from 'next/link';

export default function Navbar() {
    return (
        <nav className="w-full py-4 px-6 border-b border-gray-200 dark:border-gray-800 bg-white/50 dark:bg-black/50 backdrop-blur-md fixed top-0 z-50">
            <div className="max-w-7xl mx-auto flex justify-between items-center">
                <Link href="/" className="text-xl font-bold tracking-tighter">
                    AI Trend Notifier
                </Link>
                <div className="flex gap-4 items-center">
                    <Link href="/newsletters" className="text-sm font-medium hover:text-accent transition-colors">
                        Newsletters
                    </Link>
                    <Link href="/login" className="text-sm font-medium hover:text-accent transition-colors">
                        Login
                    </Link>
                    <Link href="/#subscribe" className="px-4 py-2 bg-primary text-white dark:bg-white dark:text-black rounded-full text-sm font-medium hover:opacity-90 transition-opacity">
                        Subscribe
                    </Link>
                </div>
            </div>
        </nav>
    );
}
