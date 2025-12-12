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
        <div className="border border-gray-200 dark:border-gray-800 rounded-xl p-6 hover:shadow-lg transition-shadow bg-white dark:bg-gray-900">
            <div className="flex justify-between items-start mb-4">
                <span className="text-xs font-medium px-2 py-1 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400">
                    {date}
                </span>
                <span className={`text-xs font-medium px-2 py-1 rounded-full ${sentiment === 'Positive' ? 'bg-green-100 text-green-700' :
                        sentiment === 'Negative' ? 'bg-red-100 text-red-700' :
                            'bg-blue-100 text-blue-700'
                    }`}>
                    {sentiment}
                </span>
            </div>
            <h3 className="text-xl font-bold mb-2">{title}</h3>
            <p className="text-gray-600 dark:text-gray-400 mb-4 line-clamp-3">
                {summary}
            </p>
            <Link href={`/newsletters/${id}`} className="text-accent font-medium hover:underline text-sm">
                Read more →
            </Link>
        </div>
    );
}
