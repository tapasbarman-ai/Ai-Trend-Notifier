import SubscribeForm from './SubscribeForm';

export default function Hero() {
    return (
        <section className="py-20 px-6 text-center">
            <div className="max-w-3xl mx-auto space-y-8">
                <h1 className="text-5xl md:text-6xl font-bold tracking-tighter bg-clip-text text-transparent bg-gradient-to-r from-primary to-accent dark:from-white dark:to-gray-400">
                    Master the Future of AI
                </h1>
                <p className="text-xl text-gray-600 dark:text-gray-400 leading-relaxed">
                    Get the most important AI trends, tools, and insights delivered straight to your inbox.
                    No noise, just signal.
                </p>
                <SubscribeForm />
            </div>
        </section>
    );
}
