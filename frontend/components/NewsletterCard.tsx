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
        <article className="group bg-surface-container-lowest border border-outline-variant rounded-2xl overflow-hidden hover:-translate-y-2 hover:border-primary hover:shadow-xl transition-all duration-300 flex flex-col justify-between h-full">
            <div>
                {/* Illustrative Pattern Card Header */}
                <div className="aspect-video relative overflow-hidden bg-gradient-to-br from-surface-container-low via-surface-container to-surface-container-highest flex items-center justify-center border-b border-outline-variant p-6">
                    <div className="text-center space-y-2">
                        <div className="w-12 h-12 rounded-xl bg-primary-container flex items-center justify-center mx-auto text-primary font-bold shadow-sm">
                            {title.slice(0, 2).toUpperCase()}
                        </div>
                        <span className="text-[10px] uppercase font-bold text-on-surface-variant tracking-wider">edition context</span>
                    </div>
                    
                    <div className="absolute top-4 left-4">
                        <span className={`px-3 py-1 rounded-full text-[11px] font-bold shadow-sm ${
                            sentiment === 'Positive' ? 'sentiment-gradient-positive text-on-primary-container' :
                            sentiment === 'Negative' ? 'bg-error-container text-on-error-container border border-error/20' :
                            'bg-surface-container-highest text-on-surface-variant border border-outline-variant'
                        }`}>
                            {sentiment}
                        </span>
                    </div>
                </div>

                <div className="p-6 pb-0">
                    <p className="font-sans text-xs font-semibold text-on-surface-variant mb-2">{date}</p>
                    <h3 className="font-display text-lg font-bold text-on-background mb-4 group-hover:text-primary transition-colors leading-snug">
                        {title}
                    </h3>
                    
                    <div className="summary-accent p-4 mb-6 rounded-r-lg">
                        <p className="font-sans text-xs italic text-on-background leading-relaxed line-clamp-3">
                            "{summary}"
                        </p>
                    </div>
                </div>
            </div>

            <div className="px-6 pb-6">
                <Link href={`/newsletters/${id}`} className="flex items-center gap-1.5 font-sans text-label-bold font-bold text-primary group/link hover:opacity-80 transition-all text-sm w-fit">
                    Read Full Edition 
                    <span className="transition-transform duration-300 group-hover/link:translate-x-1">→</span>
                </Link>
            </div>
        </article>


    );
}
