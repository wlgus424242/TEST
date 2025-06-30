from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import telegram

# 봇 토큰 입력 (실제 토큰으로 교체)
TOKEN = "7866089066:AAGI-sq0AubwDLGAdXd6lhZv1fm57fW6nlI"

# 명령어 처리 함수 (예: /start 명령어)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("⚠️필독사항⚠️\n떡상퇴사 채팅방에 오신 것을 환영합니다🖐️\n본 소통방에 입장시 아래의 혜택들을 받으실 수 있습니다🎈\n\n✅1.매일 오전,저녁 비트코인/이더리움 실시간 시황\n\n✅2.24시간 알트코인 추천\n\n✅3.라이브 요약 방송 및 코인추천 방송\n\n✅4.1:1질의응답\n\n/help : 입장문의를 원하시면 좌측의 help를 눌러주세요")

# 명령어 처리 함수 (예: /help 명령어)
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("❌본 채널은 일절 구독자분들께 금전요구❌\n❌멤버쉽가입을 유도하고있지 않으며❌\n오로지 개인적인 관점에 의한 시황,추천만 있을뿐입니다.\n\n🔥최근 불법 유료 리딩방 업자🔥\n🔥광고업자들이 성행하고있습니다🔥\n\n광고업자들이 없는 클린한 소통방을 위해 구독자분이 맞는지\n✅✅제가 직접 더블체크를 진행하고있고✅✅\n검증이 끝난 이후 소통방에 초대해드리고있습니다.이에 동의하시면\n\n010-8204-8525\n\n제 개인 전화번호로 💌숫자 1번💌을 보내주시면 되겠습니다\n확인하는 즉시 텔레그램방 입장 도와드리겠습니다^^\n\n/sms : 원클릭 문자발송 (한번 누르시면 복사됩니다)")

# 명령어 처리 함수 (예: /sms 명령어)
async def sms_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("010-8204-8525")


def main():
    # Application 생성
    application = Application.builder().token(TOKEN).build()

    # 명령어 핸들러 등록
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("sms", sms_command))
    # 다른 명령어 핸들러 추가

    # 봇 시작
    application.run_polling()

if __name__ == "__main__":
    main()