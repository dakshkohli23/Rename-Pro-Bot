#-------------------------------------- https://github.com/dakshkohli23/Rename-Pro-Bot --------------------------------------#

class Translation( object ):
    NOT_AUTH_TXT = "<b>⚠️ Unauthorized Access ⚠️</b>\nYou're not Auth User. So You Can't Use the Core " \
                   "components of this Bot. Inconvenience is regretted!"
    DOWNLOAD_START = "<b>━━┫ Downloading 📥 ┣━━</b>"
    UPLOAD_START = "<b>━━┫ Uploading 📥 ┣━━</b>"
    SAVED_CUSTOM_THUMB_NAIL = "<b>✅ Thumbnail Saved Successfully.</b>\n<code>This file will be used in upcoming " \
                              "rename or video conversions</code> "
    SAVED_RECVD_DOC_FILE = "<b>✔️ Media Downloaded Successfully</b>"
    ACCESS_DENIED_TEXT = "You're not Authorized to use this Bot."
    START_TEXT = "Hey.. <b>{}</b>\n\n<b>I'm -</b> {}\n\n<b>Things I Can Do:</b>\n" \
                 "➟ Rename File \n➟ Convert to Video/File \n➟ Custom Thumbnail \n➟ Send Media to 5 Different Channels/Groups \n\n" \
                 "<i>Send filename + extension (Eg: onepiece.mkv) as a reply to any telegram media, and follow " \
                 "Bot's instructions.</i>\n\n" \
                 "<b>👨‍💻 Developer: </b><a href='https://t.me/Dlaize'> Mr. Dlaize</a>\n" \
                 "<b>🧬 Source Code: </b><a href='https://github.com/dakshkohli23/Rename-Pro-Bot'> Github</a>\n\n"
    SETTINGS_TEXT = "<b>These are my available options:</b>"
    THUMB_CAPTION = "<code>This image is your current thumbnail, Tap</code><b> DEL THUMB </b><code>if you wish to " \
                    "clear it !</code> "
    NO_THUMB = "⛔️ <b>No thumbnails available.</b>\n<code>Upload an image to save it !" \
               "!</code> "
    DEL_CUSTOM_THUMB_NAIL = "🗑️ <b>Thumbnail cleared successfully.</b>\n<code>Thumbnail won't be available to the " \
                            "downloading media, unless you upload an image !</code> "
    DEL_THUMB_CONFIRM = "⚠️ <b>Do you wish to remove thumbnail?</b>\n<code>Thumbnail won't be available in the files " \
                        "when you delete it!</code> "
    FILE_TYPE_SELECT = "<b>Select the format for File name:</b>\n👉 {}"
    INPUT_ERROR = "<b>⚠️ Invalid input:</b>️\n<code>Input the file name as replay to the above message and " \
                  "check the supported extensions in welcome message !</code> "
    EXTENSIONS = ['.mkv', '.mp4', '.avi', '.webm']
    NO_SPAM_MSG = "⚠️ <b>Don't Spam Here</b>\n<code>Read the welcome message for better use of this bot !</code>"
    MAKE_A_COPY_TEXT = "<b>📚 You Need a Copy ?</b>"
    CAPTION_TEXT = "<b>📁 Filename : {}</b>"
    SUCCESSFUL_SEND = "<code>Forwarded Successfully to:</code>\n<b>{}</b>"
    FORWARD_ERROR = "<b>⚠️ Attention :</b>\n<code>Make Sure That I am Admin in Your Channel or Provided Channel " \
                    "ID is Correct.</code>"
    CHANNEL_CONFIRM = "<b>⚠️ Attention :</b>\n<code>Now I'll send messages to:</code>\n\n<b>{}</b>"
    INVALID_CHANNEL = "⚠️ <b>Attention :</b>\n<code>Invalid Channel Id Selected.\nPossible Causes of this " \
                      "error:</code>\n\n1️⃣ <b>Bot is not an admin in Your Channel</b>\n\n2️⃣ <b>You haven't entered " \
                      "a valid channel id in the config ENV.</b>\n\n3️⃣ <b>You haven't set a default channel in the " \
                      "bot for the process.</b> "
    NOT_REPLIED_TO_MESSAGE = "⚠️ <b>Attention :</b>\n<code>Replay to any message to send !</code>"
    INFO_CHANNEL = "I'm currently sending messages to:\n<b>{}</b>"
    NO_DEFAULT_SET = "⚠️ <b>Attention :</b>\n<code>No Default channels found! Set a channel first.</code>"
    LIST_CHANNELS = "<b>These are my associated chats in use:</b>\n\n<b>Channel 1:</b>\n<code>ID: {}</code>\nName: {" \
                    "}\n\n<b>Channel2:</b>\n<code>ID: {}</code>\nName: {}\n\n<b>Channel 3:</b>\n<code>ID: {" \
                    "}</code>\nName: {}\n\n<b>Channel 4:</b>\n<code>ID: {}</code>\nName: {}\n\n<b>Channel " \
                    "5:</b>\n<code>ID: {}</code>\nName: {} "
    START_APP_TEXT = "⚡ {} with Pyrogram v{} (Layer {}) started on {} ⚡"
    STOP_APP_TEXT = "🚫 Bot Stopped... 🚫"
