import Link from 'next/link';

export default function Navbar() {
    return (
        <nav className="w-full py-4 px-6 border-b border-white/5 bg-darkBg/60 backdrop-blur-md fixed top-0 z-50 transition-all duration-300">
            <div className="max-w-7xl mx-auto flex justify-between items-center">
                <Link href="/" className="text-xl font-extrabold tracking-tight bg-gradient-to-r from-primary via-indigo-400 to-accent bg-clip-text text-transparent hover:opacity-90 transition-opacity">
                    AI Trend Notifier
                </Link>
                <div className="flex gap-6 items-center">
                    <Link href="/newsletters" className="text-sm font-medium text-gray-300 hover:text-white transition-colors relative group py-1">
                        Newsletters
                        <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-primary transition-all duration-300 group-hover:w-full"></span>
                    </Link>
                    <Link href="/login" className="text-sm font-medium text-gray-300 hover:text-white transition-colors relative group py-1">
                        Login
                        <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-primary transition-all duration-300 group-hover:w-full"></span>
                    </Link>
                    <Link href="/#subscribe" className="px-5 py-2 bg-gradient-to-r from-primary to-accent text-white rounded-full text-sm font-semibold hover:brightness-110 active:scale-95 transition-all shadow-lg shadow-primary/20">
                        Subscribe
                    </Link>
                </div>
            </div>
        </nav>
    );
}

