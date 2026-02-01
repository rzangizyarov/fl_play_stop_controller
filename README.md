# FL Play/Stop Controller

MIDI-скрипт для FL Studio, который позволяет переключать **Play** и **Stop** с помощью **любого MIDI-сообщения**.  
Скрипт не привязан к конкретному устройству и работает с любыми контроллерами, пэдами и другими устройствами, передающими MIDI-сообщения.

## Возможности

- Переключение **Play / Stop** производится с любого MIDI-сообщения устройства;
- Не требуется настройка сообщений Program Change, Control Change и значений;
- Работает с любым MIDI-контроллером.

## Установка

1. Перенести директорию `PlayStop Controller` в `%USERPROFILE%\Documents\Image-Line\FL Studio\Settings\Hardware`.
2. Открыть FL Studio и перейти в `Options → MIDI Settings`;
3. Выбрать MIDI-вход;
4. Изменить тип контроллера (*Controller type*) с `(generic controller)` на `Play/Stop Controller`;
5. Для возврата режима работы контроллера в обычный режим вернуть тип контроллера на `(generic controller)`.
