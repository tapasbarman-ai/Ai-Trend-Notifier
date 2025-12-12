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
        <div className="flex items-center gap-2">
            {message && <span className="text-sm text-gray-500">{message}</span>}
            <button
                onClick={handleFetch}
                disabled={loading}
                className="flex items-center gap-2 px-4 py-2 bg-secondary text-white rounded-lg text-sm font-medium hover:opacity-90 disabled:opacity-50"
            >
                {loading ? <Loader2 className="animate-spin h-4 w-4" /> : <RefreshCw className="h-4 w-4" />}
                Fetch Latest Trends
            </button>
        </div>
    );
}
