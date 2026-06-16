import SubscribeForm from './SubscribeForm';

export default function Hero() {
    return (
        <section className="py-24 px-6 text-center relative overflow-hidden">
            {/* Background glowing glow circles */}
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-primary/10 rounded-full blur-[100px] pointer-events-none"></div>
            <div className="absolute top-1/3 left-1/3 w-60 h-60 bg-accent/5 rounded-full blur-[80px] pointer-events-none"></div>

            <div className="max-w-4xl mx-auto space-y-10 relative z-10">
                <div className="space-y-4">
                    <span className="px-3 py-1 rounded-full text-xs font-semibold bg-primary/10 border border-primary/20 text-indigo-300 uppercase tracking-wider">
                        ⚡ AI-Powered Ingestion Pipeline
                    </span>
                    <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-white via-indigo-200 to-accent leading-none">
                        Master the Future of AI
                    </h1>
                </div>
                
                <p className="text-lg md:text-xl text-gray-400 max-w-2xl mx-auto leading-relaxed">
                    Get real-time AI trends, sentiment scores, and contextual summaries scraped directly from Reddit and Twitter. Delivered straight to your inbox.
                </p>
                
                <div className="max-w-md mx-auto" id="subscribe">
                    <SubscribeForm />
                </div>

                {/* Trust and status metrics */}
                <div className="grid grid-cols-3 gap-4 md:gap-8 pt-10 border-t border-white/5 max-w-3xl mx-auto text-left">
                    <div className="p-4 rounded-xl glass-card">
                        <p className="text-3xl font-extrabold text-white">1,500+</p>
                        <p className="text-xs text-gray-400 mt-1 font-medium">Subscribers</p>
                    </div>
                    <div className="p-4 rounded-xl glass-card">
                        <p className="text-3xl font-extrabold text-white">94%</p>
                        <p className="text-xs text-gray-400 mt-1 font-medium">Sentiment Accuracy</p>
                    </div>
                    <div className="p-4 rounded-xl glass-card">
                        <p className="text-3xl font-extrabold text-white">Daily</p>
                        <p className="text-xs text-gray-400 mt-1 font-medium">Digests Sent</p>
                    </div>
                </div>
            </div>
        </section>
    );
}

