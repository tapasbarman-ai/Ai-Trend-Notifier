import Link from 'next/link';

export default function Navbar() {
    return (
        <header className="bg-background dark:bg-inverse-surface border-b border-outline-variant dark:border-outline w-full fixed top-0 z-50 transition-all duration-300">
            <nav className="flex justify-between items-center px-6 md:px-margin-desktop py-4 max-w-container-max-width mx-auto">
                <Link href="/" className="font-display text-headline-md text-on-background dark:text-inverse-on-surface hover:opacity-90 transition-opacity">
                    AI Insights
                </Link>
                <div className="hidden md:flex gap-8 items-center font-sans text-body-md">
                    <Link href="/newsletters" className="text-on-surface-variant dark:text-surface-variant hover:text-primary transition-colors">
                        Feed
                    </Link>
                    <Link href="/newsletters" className="text-on-surface-variant dark:text-surface-variant hover:text-primary transition-colors">
                        Archive
                    </Link>
                    <Link href="/#subscribe" className="text-on-surface-variant dark:text-surface-variant hover:text-primary transition-colors">
                        Subscribe
                    </Link>
                </div>
                <div className="flex items-center gap-6">
                    <Link href="/login" className="scale-95 active:scale-90 transition-transform text-primary dark:text-primary-fixed font-sans text-label-bold hover:opacity-85">
                        Sign In
                    </Link>
                    <Link href="/#subscribe" className="bg-primary-container text-on-primary-container px-6 py-2.5 rounded-full font-sans text-label-bold hover:translate-y-[-2px] transition-all glow-yellow-sm hover:bg-primary-container/90">
                        Get Started
                    </Link>
                </div>
            </nav>
        </header>
    );
}
