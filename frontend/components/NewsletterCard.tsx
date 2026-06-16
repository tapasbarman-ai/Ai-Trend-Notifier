import Link from 'next/link';

interface NewsletterProps {
    id: number;
    title: string;
    summary: string;
    sentiment: string;
    published_at: string;
}

export default function NewsletterCard({ id, title, summary, sentiment, published_at }: NewsletterProps) {
    const date = new Date(published_at).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    });

    return (
        <div className="glass-card rounded-2xl p-6 flex flex-col justify-between h-full hover:border-primary/20">
            <div>
                <div className="flex justify-between items-center mb-4">
                    <span className="text-xs font-semibold text-gray-500">
                        {date}
                    </span>
                    <span className={`text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full ${
                        sentiment === 'Positive' ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 shadow-[0_0_12px_rgba(16,185,129,0.05)]' :
                        sentiment === 'Negative' ? 'bg-rose-500/10 text-rose-400 border border-rose-500/20 shadow-[0_0_12px_rgba(244,63,94,0.05)]' :
                        'bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 shadow-[0_0_12px_rgba(99,102,241,0.05)]'
                    }`}>
                        {sentiment}
                    </span>
                </div>
                <h3 className="text-xl font-bold text-white mb-2 line-clamp-2 leading-snug">{title}</h3>
                <p className="text-sm text-gray-400 mb-6 line-clamp-3 leading-relaxed">
                    {summary}
                </p>
            </div>
            <Link href={`/newsletters/${id}`} className="text-primary hover:text-white font-semibold flex items-center gap-1 text-sm transition-colors group/link w-fit">
                Read edition
                <span className="transition-transform duration-300 group-hover/link:translate-x-1">→</span>
            </Link>
        </div>

    );
}
