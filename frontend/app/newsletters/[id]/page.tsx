'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import api from '@/utils/api';
import { Loader2, ArrowLeft } from 'lucide-react';

interface Newsletter {
    id: number;
    title: string;
    summary: string;
    content: string;
    sentiment: string;
    published_at: string;
}

export default function NewsletterDetailPage() {
    const params = useParams();
    const router = useRouter();
    const [newsletter, setNewsletter] = useState<Newsletter | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchNewsletter = async () => {
            try {
                const response = await api.get(`/newsletters/${params.id}`);
                setNewsletter(response.data);
            } catch (error) {
                console.error('Failed to fetch newsletter', error);
            } finally {
                setLoading(false);
            }
        };

        if (params.id) {
            fetchNewsletter();
        }
    }, [params.id]);

    if (loading) {
        return (
            <div className="flex justify-center items-center min-h-[50vh]">
                <Loader2 className="animate-spin h-8 w-8 text-gray-400" />
            </div>
        );
    }

    if (!newsletter) {
        return (
            <div className="max-w-4xl mx-auto px-6 py-12 text-center">
                <h1 className="text-2xl font-bold mb-4">Newsletter Not Found</h1>
                <button
                    onClick={() => router.push('/newsletters')}
                    className="text-accent hover:underline"
                >
                    ← Back to Newsletters
                </button>
            </div>
        );
    }

    const date = new Date(newsletter.published_at).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    });

    return (
        <div className="max-w-4xl mx-auto px-6 py-12">
            <button
                onClick={() => router.push('/newsletters')}
                className="flex items-center gap-2 text-gray-600 dark:text-gray-400 hover:text-accent mb-8"
            >
                <ArrowLeft className="h-4 w-4" />
                Back to Newsletters
            </button>

            <article className="prose prose-lg dark:prose-invert max-w-none">
                <div className="flex items-center gap-4 mb-4">
                    <span className="text-sm text-gray-500">{date}</span>
                    <span className={`text-xs font-medium px-3 py-1 rounded-full ${newsletter.sentiment === 'Positive' ? 'bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300' :
                            newsletter.sentiment === 'Negative' ? 'bg-red-100 text-red-700 dark:bg-red-900 dark:text-red-300' :
                                'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300'
                        }`}>
                        {newsletter.sentiment}
                    </span>
                </div>

                <h1 className="text-4xl font-bold mb-6">{newsletter.title}</h1>

                <div className="bg-gray-50 dark:bg-gray-900 border-l-4 border-accent p-6 mb-8 rounded-r-lg">
                    <p className="text-lg font-medium text-gray-700 dark:text-gray-300">
                        {newsletter.summary}
                    </p>
                </div>

                <div className="whitespace-pre-wrap text-gray-800 dark:text-gray-200">
                    {newsletter.content}
                </div>
            </article>
        </div>
    );
}
