import "reflect-metadata";
import TelegramBot from "node-telegram-bot-api";

// توکن را از Railway Variables بگیر
const TOKEN = process.env.BOT_TOKEN;

if (!TOKEN) {
  throw new Error("BOT_TOKEN is not defined in environment variables");
}

// ساخت ربات
const bot = new TelegramBot(TOKEN, { polling: true });

// 🟢 شروع ربات
bot.onText(/\/start/, (msg) => {
  bot.sendMessage(
    msg.chat.id,
    "🤖 WA.io Bot فعال است!\n\nبرای ارسال پیام از /post استفاده کن"
  );
});

// 📢 ارسال پیام ساده
bot.onText(/\/post (.+)/, (msg, match) => {
  const chatId = msg.chat.id;
  const text = match?.[1];

  if (!text) {
    bot.sendMessage(chatId, "❌ متن را وارد کن");
    return;
  }

  bot.sendMessage(chatId, `📢 پیام شما:\n\n${text}`);
});

// 🧠 کنترل پیام‌های عادی
bot.on("message", (msg) => {
  if (msg.text?.startsWith("/")) return;

  bot.sendMessage(
    msg.chat.id,
    "⚡ WA.io دریافت کرد:\n" + msg.text
  );
});

console.log("🤖 WA.io Bot is running...");
