# 祝日法の制定・初回改正 再構築試行結果

2026-11-16（日本時間）。[作業手順](rebuild-plan.md)を先に作成し、その後に原典取得とデータ作成を実施した。

## 結果

制定時 `ry273we4` と、昭和41年法律第86号による改正後 `gfah5dqe` の2版を作成した。各版は本則3条と制定附則2項を持つ。第二條の表は9行から12行になり、元の9行・本則の他の部分・制定附則はバイト単位で同じである。

改正で追加した行は、成人の日の後の建国記念の日、こどもの日の後の敬老の日、秋分の日の後の体育の日。建国記念の日の欄は「政令で定める日」を保存した。改正法の附則を被改正法本文へ転記していない。

Revision IDはsecrets.choiceでCrockford Base32小文字8字をランダム発行し、既存版ディレクトリと衝突しないことを確認した。表の12行のkeyも同じ文字集合の4字をランダム発行し、既存9行のkeyを改正後へ維持した。発行結果は[スナップショット](trial-snapshot.json)に記録した。

## 原典取得と照合

画像の取得URL・取得日・SHA-256は[取得記録](sources/downloads.json)に保存した。原寸JPEGとIIIFマニフェストを同じフォルダに保存し、Source.fixedにも画像のハッシュを記録した。

| 資料 | 今回閲覧した範囲 | 判断・用途 |
|---|---|---|
| [官報第6453号・1948-07-20](https://dl.ndl.go.jp/pid/2962986) | 1コマ、117頁、法律第百七十八号の題名・本則・附則・公布日 | 制定本文と施行の主たる根拠。國・條と新字体が混在すること、表9行、附則2項を確認 |
| [官報第6512号・1948-09-28](https://dl.ndl.go.jp/pid/2963048) | 2コマ、218頁下段の正誤。原寸画像から切り出したcorrection-detail.pngでも確認 | 第二條八行の「國民の」を「國の」に訂正する指示を確認 |
| [制定御署名原本・御31171100](https://www.digital.archives.go.jp/file/130738) | 2・3画像の本則・附則。1画像は保存のみ | 官報で細部が不鮮明な「豊」「号」等の照合補助。憲法記念日の欄が「國の成長」であることを確認 |
| [改正御署名原本・御42643100](https://www.digital.archives.go.jp/file/686000) | 1画像の公布文日付、2画像の改め文と追加3行、3画像の附則第一項 | 公布の日から施行すること、追加行の位置・字句を確認。2画像の「二月十一日」の見え消しと手書き訂正をsourceEditとして注記 |

昭和41年6月25日官報号外第78号は検索したが、今回利用できる公開画像を取得できなかった。号の手がかりは[国立国会図書館レファレンス協同データベース](https://crd.ndl.go.jp/reference/entry/reference/show?id=1000025574)にある。御署名原本で代替し、REB-05に従って官報の字体照合・官報正誤は未確認とした。官報が存在しないという判断ではない。

既存のloj-spec hist-001試作は、資料探索・Markdown/YAML構造・字体注記の下書きとして使用した。本文は今回取得した上記画像と照合した。改正後全文の複写はせず、制定版に今回読んだ3行を挿入して作成した。下書きはsrc-draftとして明示し、text.sourcesには含めていない。

字体は、すべての字のUnicode対応を確定したわけではない。「祝」の統合漢字と互換漢字、数字の幅、「労／勞」「産／產」等を注記した。試作から引き継いだ曖昧字の判断を今回の確認済み主張とせず、注記のverificationをunverifiedにした。両版のglyphCheckもunverifiedである。新旧字体変換・Unicode正規化は適用していない。

官報正誤の「國の成長」は同じ制定Revisionに反映し、資料間の違いと解消根拠をtext.variancesにも記録した。今回確認したのは1948-09-28の正誤であり、他の日付の正誤を網羅したとはいえないためcorrectionsSurveyedはunsurveyedとして具体的理由を残した。

## 旧履歴と登録

- 旧master凍結候補：09710a8ea128543b04627eb70e353b9675c27177。
- 旧origin/not_entered_into_force：da2424f55c5d180424d32cbcc142860b7636cc3f。平成30年改正はこのブランチに実在する。仕様の試作の「旧commitがない」という記録を改めた。
- 旧履歴13commitを3件のmappingsと10件のpendingで漏れなく記録した。対応判断は全文・全字体の照合未完了としてunverifiedにした。
- 旧本文のリストから表への構造変更、原典にない附則見出し、字体の差、改正附則リンクの除外をrebuild.yamlに記録した。
- 別リポジトリloj-registryに本法と改正法を登録した。改正法はnotCollectedとし、既存のREADMEのみの改正法リポジトリには変更を加えていない。旧名称19660625-law-86は旧本文のリンクを根拠にaliasesへ記録した。
- 台帳のcanonicalBranch: mainは本移行後の構成案であり、現在リモートに公開された正本を表すものとしては使わない。

ローカル試行完了時点では未コミットだった。その後、利用者の指示により本法・台帳のtrial/holiday-rebuild-20261116を公開する。旧masterと旧not_entered_into_forceの先端を保持し、mainへのマージは行わない。リモートの旧ブランチを保護設定で凍結したという意味ではない。空だった台帳リポジトリでは最初に公開する試行ブランチが既定となるが、正本mainとは区別する。

## 検査

仕様commitはb200fdb13957c6d6c7f9805d59c78980abac093d。検査器のvendor/loj-spec/COMMITと一致する。検査器checkoutは10b0a3d1ca119db03129479a01caff66743bf430。使用した実行ファイルのSHA-256は[provenance.json](validation/provenance.json)に記録した。checkoutのHEADだけではそのバイナリのビルド元を証明しない。

| 検査 | 結果 |
|---|---|
| 制定版L0 / L1 | 両方pass |
| 改正後版L0 / L1 | 両方pass |
| L3 historyStructure / evidence | 両方pass |
| 登録台帳registry | pass |
| L4 relationResolution / relationConsistency / timeConsistency / displayConsistency | すべてpass |
| 再構築報告rebuild | pass |
| 原典画像SHA-256、追加3行の内容・位置、既存9行、他の本則、制定附則、旧refs | すべて確認 |

L3にはTIME-03の警告が5件ある。L4の診断は0件。施行日のderived値にcalcを設定していないため、検査器はその日付を計算検証していない。公布の日から施行することと日付は画像の該当箇所で確認したが、1966年の官報発行日との照合は未了。警告を隠すために根拠や確認状態を変えていない。

初回のregistry単独呼出しは引数の組合せで終了コード2となり、ディレクトリを位置引数に修正して再実行した。保存したJSONは最終の検査結果である。

[再実行スクリプト](verify-trial.py)はPython標準ライブラリのみで実行できる。workspace直下から：

```powershell
python 19480720-law-178/docs/verify-trial.py
```

[実行コマンドと結果](validation/commands.json)、[本文差分等の確認](validation/invariants.json)、各レベルのJSON報告をvalidation/に保存した。target.commitは空文字のディレクトリ検査であり、正本の特定commitへの適合認証ではない。L3 evidenceの合格も画像の内容と転記の一致を機械的に証明するものではない。

## 残る作業

1. 昭和41年官報画像の入手・御署名原本との照合、および両時期の官報正誤の追加調査。
2. 字体の細部の再照合と、旧commitとRevisionの対応の全文確認。
3. 本移行時には旧URLの保持方針を確認し、mainの起点・変更種別trailer付きcommit・PRを準備して、正本commitを対象にした検査を行う。試行版の公開時にはchange検査を別途実施する。mainへ未統合のため固定参照の検査は対象外。
4. 後続10改正と、全履歴の網羅性・適用条件の調査。coverage: unconfirmed、applicability: unsurveyedを維持する。

Claude Codeは作業者として2回起動を試みたが、最終的にログイン期限切れによるauthentication_failedを確認した。Claude Codeによるファイル変更はなく、以後の再構築・原典確認・検査はCodexが実施した。

## 試行版の公開

利用者の指示により試行ブランチを公開する。本文・履歴をrevisionAdd、字体注記・下書き資料・再構築報告をmetadata、登録台帳をmetadataとして記録した。[変更検査](publication-validation/commits.json)は両リポジトリでpass。法令データは710b30fとa00529c、台帳データは77bae8aのコミットに収録している。台帳の起点26754ecはREADMEのみで、データ変更の分類対象外である。

下書き資料src-draftをrevisionAddへ含めた最初の構成はCHG-02で不合格となったため、未公開の作業コミットを組み直してmetadataへ分離した。検査合格後の記録だけを公開する。作業ブランチのコミットIDは正本の固定参照ではない。ここでの公開は正本移行ではなく、試行成果の共有である。

原典画像とYAML・本文のバイト列を維持するため.gitattributesでGitの改行変換を無効にした。検査コマンドに含まれる作業ディレクトリは公開用に相対パスへ変更した。
