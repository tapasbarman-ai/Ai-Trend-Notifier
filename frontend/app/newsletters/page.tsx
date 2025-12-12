'use client';

import { useEffect, useState } from 'react';
import api from '@/utils/api';
import NewsletterCard from '@/components/NewsletterCard';
import { Loader2 } from 'lucide-react';

interface Newsletter {
    id: number;
    title: string;
    summary: string;
    content: string;
    sentiment: string;
    published_at: string;
}

export default function NewslettersPage() {
    const [newsletters, setNewsletters] = useState<Newsletter[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchNewsletters = async () => {
            try {
                const response = await api.get('/newsletters/');
                setNewsletters(response.data);
            } catch (error) {
                console.error('Failed to fetch newsletters', error);
            } finally {
                setLoading(false);
            }
        };
        fetchNewsletters();
    }, []);

    if (loading) {
        return (
            <div className="flex justify-center items-center min-h-[50vh]">
                <Loader2 className="animate-spin h-8 w-8 text-gray-400" />
            </div>
        );
    }

    return (
        <div className="max-w-4xl mx-auto px-6 py-12">
            <h1 className="text-3xl font-bold mb-8">Latest Editions</h1>
            <div className="grid gap-6 md:grid-cols-2">
                {newsletters.map((newsletter) => (
                    <NewsletterCard
                        key={newsletter.id}
                        id={newsletter.id}
                        title={newsletter.title}
                        summary={newsletter.summary}
                        sentiment={newsletter.sentiment}
                        published_at={newsletter.published_at}
                    />
                ))}
            </div>
            {newsletters.length === 0 && (
                <p className="text-center text-gray-500">No newsletters published yet.</p>
            )}
        </div>
    );
}
