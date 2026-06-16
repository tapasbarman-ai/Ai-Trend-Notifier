'use client';

import { useState } from 'react';
import api from '@/utils/api';
import { Loader2, RefreshCw } from 'lucide-react';

export default function FetchTrendsButton() {
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('');

    const handleFetch = async () => {
        setLoading(true);
        setMessage('');
        try {
            await api.post('/pipeline/run');
            setMessage('Pipeline started in background.');
        } catch (error) {
            setMessage('Failed to start pipeline.');
        } finally {
            setLoading(false);
            setTimeout(() => setMessage(''), 3000);
        }
    };

    return (
        <div className="flex items-center gap-4">
            {message && (
                <span className="text-xs text-indigo-300 font-semibold bg-primary/10 border border-primary/20 px-3 py-1.5 rounded-lg animate-pulse">
                    {message}
                </span>
            )}
            <button
                onClick={handleFetch}
                disabled={loading}
                className="flex items-center gap-2 px-4 py-2.5 bg-white/5 border border-white/10 text-white rounded-lg text-sm font-semibold hover:bg-white/10 hover:border-white/20 active:scale-95 transition-all disabled:opacity-50"
            >
                {loading ? <Loader2 className="animate-spin h-4 w-4 text-primary" /> : <RefreshCw className="h-4 w-4" />}
                Fetch Latest Trends
            </button>
        </div>

    );
}
