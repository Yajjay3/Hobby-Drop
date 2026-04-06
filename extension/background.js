/**
 * Background service worker for Hobby Drop
 *
 * - Sets a daily alarm to remind users to check their fact
 * - Shows a notification when the alarm fires
 * - Syncs paid status from ExtensionPay
 */

if (typeof importScripts === 'function') {
  importScripts('ExtPay.js');
}

const EXTPAY_EXTENSION_ID = 'hobby-drop';
const extpay = ExtPay(EXTPAY_EXTENSION_ID);
extpay.startBackground();

const syncPremiumStatus = async () => {
  try {
    const user = await ExtPay(EXTPAY_EXTENSION_ID).getUser();
    const isPremium = Boolean(user?.paid);

    await chrome.storage.sync.set({
      isPremium,
      premiumPlanInterval: user?.plan?.interval || null,
      premiumEmail: user?.email || null,
    });

    return isPremium;
  } catch (error) {
    console.warn('ExtensionPay status sync failed:', error);
    return false;
  }
};

// ── Install / Update ────────────────────────────────────────────
chrome.runtime.onInstalled.addListener(async () => {
  chrome.alarms.create('dailyDrop', { periodInMinutes: 1440 });
  await syncPremiumStatus();
});

chrome.runtime.onStartup.addListener(() => {
  syncPremiumStatus();
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message?.type === 'extpay-sync-status') {
    syncPremiumStatus()
      .then((isPremium) => sendResponse({ isPremium }))
      .catch(() => sendResponse({ isPremium: false }));
    return true;
  }

  return false;
});

// ── Alarm handler ───────────────────────────────────────────────
chrome.alarms.onAlarm.addListener(async (alarm) => {
  if (alarm.name !== 'dailyDrop') return;

  const { hobbyName } = await chrome.storage.sync.get('hobbyName');
  if (!hobbyName) return;

  chrome.notifications.create('dailyDropNotification', {
    type: 'basic',
    iconUrl: 'icons/icon128.png',
    title: 'Hobby Drop ✨',
    message: `Your daily ${hobbyName} fact is ready! Click to check it out.`,
  });
});

// ── Click notification to open popup ────────────────────────────
chrome.notifications.onClicked.addListener((notifId) => {
  if (notifId === 'dailyDropNotification') {
    chrome.action.openPopup();
  }
});
