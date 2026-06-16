'use client';

import { useState } from 'react';
import api from '@/utils/api';
import { Loader2, RefreshCw, Zap, CheckCircle2, AlertCircle } from 'lucide-react';

export default function FetchTrendsButton() {
    const [loading, setLoading] = useState(false);
    const [status, setStatus] = useState<'idle' | 'success' | 'error'>('idle');

    const handleFetch = async () => {
        setLoading(true);
        setStatus('idle');
        try {
            await api.post('/pipeline/run');
            setStatus('success');
            setTimeout(() => setStatus('idle'), 3000);
        } catch (error) {
            setStatus('error');
            setTimeout(() => setStatus('idle'), 3000);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="flex items-center gap-4">
            <button
                onClick={handleFetch}
                disabled={loading}
                className={`px-6 py-3 rounded-full font-sans text-label-bold font-bold border-2 transition-all flex items-center gap-2 hover:-translate-y-0.5 active:scale-95 disabled:opacity-75 ${
                    status === 'success'
                        ? 'bg-emerald-100 text-emerald-800 border-emerald-500'
                        : status === 'error'
                        ? 'bg-rose-100 text-rose-800 border-rose-500'
                        : 'bg-primary-container text-on-primary-container border-primary hover:shadow-lg hover:shadow-primary-container/20'
                }`}
            >
                {loading ? (
                    <>
                        <Loader2 className="animate-spin h-5 w-5" />
                        <span>Fetching...</span>
                    </>
                ) : status === 'success' ? (
                    <>
                        <CheckCircle2 className="h-5 w-5" />
                        <span>Trends Updated</span>
                    </>
                ) : status === 'error' ? (
                    <>
                        <AlertCircle className="h-5 w-5" />
                        <span>Fetch Failed</span>
                    </>
                ) : (
                    <>
                        <Zap className="h-5 w-5" />
                        <span>Fetch Latest Trends</span>
                    </>
                )}
            </button>
        </div>
    );
}
