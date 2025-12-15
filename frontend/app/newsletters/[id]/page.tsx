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

    // Parse content and enriched data
    const delimiter = "Enriched Data:";
    const parts = newsletter.content.split(delimiter);
    const mainContent = parts[0];
    let sources: any[] = [];

    if (parts.length > 1) {
        try {
            const rawSources = parts[1].trim();

            // 1. Try standard JSON parse first (for new data or lucky old data)
            try {
                sources = JSON.parse(rawSources);
            } catch (jsonError) {
                // 2. If JSON fails, it's likely the Python string format: [{'key': 'value'}, ...]
                // We need a more robust regex-based extraction that handles:
                // - Mixed quotes (single or double)
                // - Python None/True/False
                // - Unsorted keys

                // Regex to match individual dictionary items in the list: { ... }
                // This non-greedy match finds each object block
                const objectRegex = /\{[^{}]+\}/g;
                let objectMatch;

                while ((objectMatch = objectRegex.exec(rawSources)) !== null) {
                    const objStr = objectMatch[0];
                    const sourceItem: any = {};

                    // Helper to extract field value regardless of quote type
                    const extractField = (fieldName: string) => {
                        // Matches: 'key': 'value' OR 'key': "value"
                        // Captures the quote used and the content
                        const fieldRegex = new RegExp(`'${fieldName}':\\s*(['"])(.*?)\\1`, 's');
                        const match = fieldRegex.exec(objStr);
                        return match ? match[2] : '';
                    };

                    sourceItem.title = extractField('title');
                    sourceItem.url = extractField('url');
                    sourceItem.snippet = extractField('snippet');

                    if (sourceItem.url) {
                        sources.push(sourceItem);
                    }
                }
            }
        } catch (e) {
            console.error("Failed to parse enriched data sources", e);
        }
    }

    return (
        <div className="max-w-4xl mx-auto px-6 py-12">
            <button
                onClick={() => router.push('/newsletters')}
                className="flex items-center gap-2 text-gray-600 dark:text-gray-400 hover:text-accent mb-8"
            >
                <ArrowLeft className="h-4 w-4" />
                Back to Newsletters
            </button>

            <article className="prose prose-lg dark:prose-invert max-w-none mb-12">
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
                    {mainContent}
                </div>
            </article>

            {sources.length > 0 && (
                <div className="border-t pt-8 mt-8">
                    <h2 className="text-2xl font-bold mb-6 text-gray-900 dark:text-white">Sources & Related Reading</h2>
                    <div className="grid gap-4 md:grid-cols-2">
                        {sources.map((source, index) => (
                            <a
                                key={index}
                                href={source.url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="block p-4 rounded-lg border border-gray-200 dark:border-gray-700 hover:border-accent dark:hover:border-accent transition-colors bg-white dark:bg-gray-800"
                            >
                                <h3 className="font-semibold text-lg mb-2 text-gray-900 dark:text-white line-clamp-2">{source.title}</h3>
                                <p className="text-sm text-gray-600 dark:text-gray-400 line-clamp-3 mb-3">{source.snippet}</p>
                                <span className="text-xs text-accent font-medium flex items-center">
                                    Read source →
                                </span>
                            </a>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}
