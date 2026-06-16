'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import SubscribersList from '@/components/SubscribersList';
import CreateNewsletterForm from '@/components/CreateNewsletterForm';
import FetchTrendsButton from '@/components/FetchTrendsButton';
import api from '@/utils/api';
import { Loader2, Users, FileText, Activity, LogOut, LayoutDashboard } from 'lucide-react';

export default function AdminPage() {
    const router = useRouter();
    const [authorized, setAuthorized] = useState(false);
    const [stats, setStats] = useState({ subscribers: 0, newsletters: 0 });
    const [loadingStats, setLoadingStats] = useState(true);

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            router.push('/login');
        } else {
            setAuthorized(true);
            fetchStats();
        }
    }, [router]);

    const fetchStats = async () => {
        try {
            setLoadingStats(true);
            const [subRes, newsRes] = await Promise.all([
                api.get('/subscribers/'),
                api.get('/newsletters/')
            ]);
            setStats({
                subscribers: subRes.data.length,
                newsletters: newsRes.data.length
            });
        } catch (error) {
            console.error('Failed to fetch dashboard stats', error);
        } finally {
            setLoadingStats(false);
        }
    };

    const handleLogout = () => {
        localStorage.removeItem('token');
        router.push('/login');
    };

    if (!authorized) return null;

    return (
        <main className="max-w-container-max-width mx-auto px-margin-mobile md:px-margin-desktop py-12 text-on-background min-h-screen">
            {/* Top App Bar / Dashboard Header */}
            <header className="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 mb-10 pb-6 border-b border-outline-variant">
                <div className="space-y-1">
                    <div className="flex items-center gap-2 text-primary font-sans text-label-bold font-bold uppercase tracking-wider text-xs">
                        <LayoutDashboard className="h-4 w-4" />
                        Admin Panel
                    </div>
                    <h1 className="font-display text-3xl md:text-4xl font-extrabold tracking-tight text-on-background uppercase">
                        Dashboard Overview
                    </h1>
                    <p className="text-on-surface-variant font-sans text-body-md font-medium">
                        Welcome back, Administrator. Here is your platform status today.
                    </p>
                </div>
                
                <div className="flex flex-wrap items-center gap-4 w-full md:w-auto">
                    <FetchTrendsButton />
                    
                    <button
                        onClick={handleLogout}
                        className="flex items-center gap-2 px-5 py-2.5 bg-red-50 text-red-600 rounded-xl text-sm font-bold hover:bg-red-100 transition-all active:scale-95"
                    >
                        <LogOut className="h-4 w-4" />
                        Logout
                    </button>
                </div>
            </header>

            {/* Stats Grid */}
            <section className="grid grid-cols-1 md:grid-cols-3 gap-gutter mb-10">
                {/* Subscribers Stat */}
                <div className="bg-surface-container-low border border-outline-variant rounded-xl p-6 relative overflow-hidden group">
                    <div className="absolute left-0 top-0 bottom-0 w-1 bg-primary-container"></div>
                    <div className="flex justify-between items-start mb-4">
                        <span className="text-on-surface-variant font-sans text-label-bold font-bold uppercase tracking-wider text-xs">
                            Total Reach
                        </span>
                        <Users className="h-5 w-5 text-primary" />
                    </div>
                    <div className="font-display text-3xl font-extrabold mb-1">
                        {loadingStats ? (
                            <Loader2 className="h-8 w-8 animate-spin text-primary-container" />
                        ) : (
                            stats.subscribers
                        )}
                    </div>
                    <div className="font-sans text-caption text-primary font-semibold flex items-center gap-1">
                        <span>Active newsletter subscribers</span>
                    </div>
                </div>

                {/* Newsletters Stat */}
                <div className="bg-surface-container-low border border-outline-variant rounded-xl p-6 relative overflow-hidden group">
                    <div className="absolute left-0 top-0 bottom-0 w-1 bg-primary-container"></div>
                    <div className="flex justify-between items-start mb-4">
                        <span className="text-on-surface-variant font-sans text-label-bold font-bold uppercase tracking-wider text-xs">
                            Sent Campaigns
                        </span>
                        <FileText className="h-5 w-5 text-primary" />
                    </div>
                    <div className="font-display text-3xl font-extrabold mb-1">
                        {loadingStats ? (
                            <Loader2 className="h-8 w-8 animate-spin text-primary-container" />
                        ) : (
                            stats.newsletters
                        )}
                    </div>
                    <div className="font-sans text-caption text-primary font-semibold flex items-center gap-1">
                        <span>Published newsletter editions</span>
                    </div>
                </div>

                {/* Pipeline Stat */}
                <div className="bg-surface-container-low border border-outline-variant rounded-xl p-6 relative overflow-hidden">
                    <div className="absolute left-0 top-0 bottom-0 w-1 bg-primary-container"></div>
                    <div className="flex justify-between items-start mb-4">
                        <span className="text-on-surface-variant font-sans text-label-bold font-bold uppercase tracking-wider text-xs">
                            System Status
                        </span>
                        <Activity className="h-5 w-5 text-primary" />
                    </div>
                    <div className="font-display text-3xl font-extrabold mb-1 text-emerald-600 flex items-center gap-2">
                        Online
                    </div>
                    <div className="font-sans text-caption text-on-surface-variant font-medium flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                        <span>Ingestion pipeline operational</span>
                    </div>
                </div>
            </section>

            {/* Bento-grid Widgets for Create Newsletter Form & Subscribers List */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
                <section className="lg:col-span-5">
                    <CreateNewsletterForm onNewsletterCreated={fetchStats} />
                </section>
                <section className="lg:col-span-7">
                    <SubscribersList onListUpdated={fetchStats} />
                </section>
            </div>
        </main>
    );
}
